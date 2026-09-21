"""Canonical AAFA agent loop with explicit verification, recovery and termination."""
class AgentLoop:
    def __init__(self, *, state, memory, environment, capability, adapter,
                 governance, verifier, recovery, trace, history, events,
                 max_cycles=10):
        self.state=state
        self.memory=memory
        self.environment=environment
        self.capability=capability
        self.adapter=adapter
        self.governance=governance
        self.verifier=verifier
        self.recovery=recovery
        self.trace=trace
        self.history=history
        self.events=events
        self.max_cycles=max_cycles

    def _decide(self, goal, observation):
        target=goal.get("target_counter")
        current=observation.get("counter")
        if target is not None and current < target:
            return {"name":"increment","amount":1}
        return {"name":"stop","amount":0}

    def run(self, goal, authorized=True):
        observation=self.environment.observe()
        self.trace.record({"stage":"observation","value":observation})
        self.memory.remember({"stage":"observation","value":observation})
        self.state.set("observation", observation)

        for cycle in range(1, self.max_cycles+1):
            decision=self._decide(goal, observation)
            self.trace.record({"stage":"decision","cycle":cycle,"value":decision})
            self.history.append({"stage":"decision","cycle":cycle,"value":decision})

            if decision["name"] == "stop":
                verification=self.verifier.verify(goal, observation)
                self.trace.record({"stage":"verification","cycle":cycle,"value":verification})
                self.history.append({"stage":"verification","cycle":cycle,"value":verification})
                status="success" if verification["verified"] else "failure"
                result={"status":status,"cycle":cycle,"verification":verification}
                self.events.emit({"type":"termination","payload":result})
                return result

            action=self.capability.invoke({"name":decision["name"],"amount":decision["amount"]})
            if action.get("status") != "success":
                result={"status":"failure","error":"capability_contract_violation","cycle":cycle}
                self.events.emit({"type":"capability_denied","payload":result})
                return result

            if not self.governance.authorize_execution(authorized, decision):
                result={"status":"failure","error":"unauthorized","cycle":cycle}
                self.events.emit({"type":"execution_denied","payload":result})
                self.history.append({"stage":"result","value":result})
                return result

            execution=self.adapter.execute(action)
            self.trace.record({"stage":"action","cycle":cycle,"value":execution})
            self.history.append({"stage":"action","cycle":cycle,"value":execution})

            environment_result=self.environment.apply(decision)
            observation=self.environment.observe()
            self.trace.record({"stage":"observation","cycle":cycle,"value":observation})
            self.history.append({"stage":"observation","cycle":cycle,"value":observation})
            self.memory.remember({"stage":"cycle","cycle":cycle,"observation":observation,
                                  "environment_result":environment_result})
            self.state.set("observation", observation)

            if environment_result.get("status") != "success":
                recovery_result=self.recovery.recover(environment_result, self.state.snapshot())
                self.trace.record({"stage":"recovery","cycle":cycle,"value":recovery_result})
                self.history.append({"stage":"recovery","cycle":cycle,"value":recovery_result})
                if not recovery_result.get("retry_allowed"):
                    return {"status":"failure","error":"environment_failure","recovery":recovery_result}
                environment_result=self.environment.apply(decision)
                observation=self.environment.observe()
                self.trace.record({"stage":"recovery_resume","cycle":cycle,"value":observation})
                self.history.append({"stage":"recovery_resume","cycle":cycle,"value":observation})
                self.state.set("observation", observation)
                if environment_result.get("status") != "success":
                    return {"status":"failure","error":"recovery_failed","recovery":recovery_result}

            evaluation={"target":goal.get("target_counter"),"observed":observation.get("counter")}
            self.trace.record({"stage":"evaluation","cycle":cycle,"value":evaluation})
            self.history.append({"stage":"evaluation","cycle":cycle,"value":evaluation})

        result={"status":"failure","error":"iteration_limit","cycle":self.max_cycles}
        self.events.emit({"type":"termination","payload":result})
        return result
