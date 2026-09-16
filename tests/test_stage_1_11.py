def test_stage_foundation_imports():
    from core.contracts.contracts import Contract
    from runtime.state.store import StateStore
    from runtime.events.bus import EventBus
    from agents.base import Agent
    from capabilities.base import Capability
    from adapters.base import Adapter
    assert Contract('x').version == '1.0'
    assert StateStore().get('missing') is None
    assert Agent('a').name == 'a'
    assert Capability('c').name == 'c'
    assert Adapter('a').name == 'a'


def test_state_event_separation():
    from runtime.state.store import StateStore
    from runtime.events.bus import EventBus
    s=StateStore(); e=EventBus(); s.set('x',1); e.emit({'type':'changed'})
    assert s.get('x') == 1 and len(e.events)==1


def test_recovery_status_transparency():
    from runtime.recovery.recovery import RecoveryPolicy
    p=RecoveryPolicy(); assert p.classify('partial')=='partial'; assert p.classify('unknown')=='unknown'
