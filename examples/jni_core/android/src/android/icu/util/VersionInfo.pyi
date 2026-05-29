from typing import Any, ClassVar, overload

class VersionInfo:
    ICU_VERSION: ClassVar["VersionInfo"]
    UCOL_BUILDER_VERSION: ClassVar["VersionInfo"]
    UCOL_RUNTIME_VERSION: ClassVar["VersionInfo"]
    UNICODE_10_0: ClassVar["VersionInfo"]
    UNICODE_11_0: ClassVar["VersionInfo"]
    UNICODE_12_0: ClassVar["VersionInfo"]
    UNICODE_12_1: ClassVar["VersionInfo"]
    UNICODE_13_0: ClassVar["VersionInfo"]
    UNICODE_14_0: ClassVar["VersionInfo"]
    UNICODE_15_0: ClassVar["VersionInfo"]
    UNICODE_15_1: ClassVar["VersionInfo"]
    UNICODE_16_0: ClassVar["VersionInfo"]
    UNICODE_1_0: ClassVar["VersionInfo"]
    UNICODE_1_0_1: ClassVar["VersionInfo"]
    UNICODE_1_1_0: ClassVar["VersionInfo"]
    UNICODE_1_1_5: ClassVar["VersionInfo"]
    UNICODE_2_0: ClassVar["VersionInfo"]
    UNICODE_2_1_2: ClassVar["VersionInfo"]
    UNICODE_2_1_5: ClassVar["VersionInfo"]
    UNICODE_2_1_8: ClassVar["VersionInfo"]
    UNICODE_2_1_9: ClassVar["VersionInfo"]
    UNICODE_3_0: ClassVar["VersionInfo"]
    UNICODE_3_0_1: ClassVar["VersionInfo"]
    UNICODE_3_1_0: ClassVar["VersionInfo"]
    UNICODE_3_1_1: ClassVar["VersionInfo"]
    UNICODE_3_2: ClassVar["VersionInfo"]
    UNICODE_4_0: ClassVar["VersionInfo"]
    UNICODE_4_0_1: ClassVar["VersionInfo"]
    UNICODE_4_1: ClassVar["VersionInfo"]
    UNICODE_5_0: ClassVar["VersionInfo"]
    UNICODE_5_1: ClassVar["VersionInfo"]
    UNICODE_5_2: ClassVar["VersionInfo"]
    UNICODE_6_0: ClassVar["VersionInfo"]
    UNICODE_6_1: ClassVar["VersionInfo"]
    UNICODE_6_2: ClassVar["VersionInfo"]
    UNICODE_6_3: ClassVar["VersionInfo"]
    UNICODE_7_0: ClassVar["VersionInfo"]
    UNICODE_8_0: ClassVar["VersionInfo"]
    UNICODE_9_0: ClassVar["VersionInfo"]
    def getMicro(self) -> int: ...
    def getMilli(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    def compareTo(self, p0: "VersionInfo") -> int: ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int, p2: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int, p2: int, p3: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: str) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int) -> "VersionInfo": ...
    def getMinor(self) -> int: ...
    def getMajor(self) -> int: ...
