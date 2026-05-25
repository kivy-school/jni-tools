from typing import Any, ClassVar, overload
from android.content.Context import Context

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RegisteredHandler:
    """Forward declaration for ``com.onesignal.PushRegistrator.RegisteredHandler``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.PushRegistrator.RegisteredHandler')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class PushRegistratorADM:
    def __init__(self) -> None: ...
    def registerForPush(self, arg0: Context, arg1: str, arg2: RegisteredHandler) -> None: ...
    @staticmethod
    def fireCallback(arg0: str) -> None: ...
