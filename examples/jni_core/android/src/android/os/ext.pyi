from typing import Any, ClassVar, overload

class SdkExtensions:
    AD_SERVICES: ClassVar[int]
    @staticmethod
    def getExtensionVersion(p0: int) -> int: ...
    @staticmethod
    def getAllExtensionVersions() -> dict: ...

