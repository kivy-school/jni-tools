from typing import Any, ClassVar, overload

class KeyRep:
    def __init__(self, arg0: "Type", arg1: str, arg2: str, arg3: list[int]) -> None: ...
    def readResolve(self) -> Any: ...

    class Type:
        SECRET: ClassVar["Type"]
        PUBLIC: ClassVar["Type"]
        PRIVATE: ClassVar["Type"]
        @staticmethod
        def values() -> list["Type"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Type": ...
