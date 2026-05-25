from typing import Any, ClassVar, overload

class AdValue:
    def getPrecisionType(self) -> int: ...
    def getCurrencyCode(self) -> str: ...
    def getValueMicros(self) -> int: ...
    @staticmethod
    def zza(arg0: int, arg1: str, arg2: int) -> "AdValue": ...

    class PrecisionType:
        UNKNOWN: ClassVar[int]
        ESTIMATED: ClassVar[int]
        PUBLISHER_PROVIDED: ClassVar[int]
        PRECISE: ClassVar[int]
