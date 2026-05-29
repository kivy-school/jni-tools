from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class IpSecAlgorithm:
    AUTH_AES_CMAC: ClassVar[str]
    AUTH_AES_XCBC: ClassVar[str]
    AUTH_CRYPT_AES_GCM: ClassVar[str]
    AUTH_CRYPT_CHACHA20_POLY1305: ClassVar[str]
    AUTH_HMAC_MD5: ClassVar[str]
    AUTH_HMAC_SHA1: ClassVar[str]
    AUTH_HMAC_SHA256: ClassVar[str]
    AUTH_HMAC_SHA384: ClassVar[str]
    AUTH_HMAC_SHA512: ClassVar[str]
    CREATOR: ClassVar[Any]
    CRYPT_AES_CBC: ClassVar[str]
    CRYPT_AES_CTR: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: Any) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Any, p2: int) -> None: ...
    def getTruncationLengthBits(self) -> int: ...
    @staticmethod
    def getSupportedAlgorithms() -> set: ...
    def getName(self) -> str: ...
    def toString(self) -> str: ...
    def getKey(self) -> Any: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
