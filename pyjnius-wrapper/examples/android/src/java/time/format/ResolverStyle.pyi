from typing import Any, ClassVar, overload

class ResolverStyle:
    STRICT: ClassVar["ResolverStyle"]
    SMART: ClassVar["ResolverStyle"]
    LENIENT: ClassVar["ResolverStyle"]
    @staticmethod
    def values() -> list["ResolverStyle"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "ResolverStyle": ...
