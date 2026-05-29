from typing import Any, ClassVar, overload

class SdkExtensions:
    AD_SERVICES: ClassVar[int]
    @staticmethod
    def getAllExtensionVersions() -> dict: ...
    @staticmethod
    def getExtensionVersion(p0: int) -> int: ...
