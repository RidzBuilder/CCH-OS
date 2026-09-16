class WorkflowEngine:
    def run(self,steps):
        results=[]
        for step in steps: results.append(step())
        return results
