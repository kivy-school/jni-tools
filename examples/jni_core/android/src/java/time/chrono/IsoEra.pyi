from typing import Any, ClassVar, overload

class IsoEra:
    BCE: ClassVar["IsoEra"]
    CE: ClassVar["IsoEra"]
    BCE: ClassVar["IsoEra"]
    CE: ClassVar["IsoEra"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "IsoEra": ...
    @staticmethod
    def of(p0: int) -> "IsoEra": ...
    def getValue(self) -> int: ...
