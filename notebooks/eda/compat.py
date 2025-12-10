# compat.py
import inspect

if not hasattr(inspect, 'getargspec'):
    def getargspec(func):
        """Backward compatibility wrapper for inspect.getargspec"""
        sig = inspect.signature(func)
        args = [
            p.name for p in sig.parameters.values()
            if p.kind == p.POSITIONAL_OR_KEYWORD
        ]
        varargs = [
            p.name for p in sig.parameters.values()
            if p.kind == p.VAR_POSITIONAL
        ]
        varargs = varargs[0] if varargs else None
        keywords = [
            p.name for p in sig.parameters.values()
            if p.kind == p.VAR_KEYWORD
        ]
        keywords = keywords[0] if keywords else None
        defaults = [
            p.default for p in sig.parameters.values()
            if p.default is not p.empty and p.kind == p.POSITIONAL_OR_KEYWORD
        ]
        return inspect.ArgSpec(args, varargs, keywords, defaults)

    inspect.getargspec = getargspec