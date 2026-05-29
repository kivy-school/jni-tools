from typing import Any, ClassVar, overload

class ResolverStyle:
    STRICT: ClassVar["ResolverStyle"]
    SMART: ClassVar["ResolverStyle"]
    LENIENT: ClassVar["ResolverStyle"]
    STRICT: ClassVar["ResolverStyle"]
    SMART: ClassVar["ResolverStyle"]
    LENIENT: ClassVar["ResolverStyle"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ResolverStyle": ...
