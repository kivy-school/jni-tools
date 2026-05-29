from typing import Any, ClassVar, overload

class AdFormat:
    BANNER: ClassVar["AdFormat"]
    INTERSTITIAL: ClassVar["AdFormat"]
    REWARDED: ClassVar["AdFormat"]
    REWARDED_INTERSTITIAL: ClassVar["AdFormat"]
    NATIVE: ClassVar["AdFormat"]
    APP_OPEN_AD: ClassVar["AdFormat"]
    @staticmethod
    def values() -> list["AdFormat"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AdFormat": ...
    def getValue(self) -> int: ...
    @staticmethod
    def getAdFormat(arg0: int) -> "AdFormat": ...
