from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Runnable:
    """Forward declaration for ``java.lang.Runnable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Runnable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html
    """
    ...

class CallbackThreadManager:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getPreference(self) -> "UseThread": ...
        def setPreference(self, arg0: "UseThread") -> None: ...
        def runOnPreferred(self, arg0: Runnable) -> None: ...

        class WhenMappings:
            ...

    class UseThread:
        MainUI: ClassVar["UseThread"]
        Background: ClassVar["UseThread"]
        @staticmethod
        def values() -> list["UseThread"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "UseThread": ...
