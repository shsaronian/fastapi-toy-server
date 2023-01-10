import contextvars

g: contextvars.ContextVar = contextvars.ContextVar("request_global",
                                                   default=None)


def has_request_context():
    return g.get() is not None
