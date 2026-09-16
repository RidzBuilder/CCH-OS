"""Stage 1 semantic model boundaries."""

class SemanticBoundaryError(ValueError): pass

def require_distinct(*values):
    if len(values)!=len({repr(v) for v in values}): raise SemanticBoundaryError("Distinct semantic values collapsed")
