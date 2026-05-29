from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

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
    CREATOR: ClassVar[Creator]
    CRYPT_AES_CBC: ClassVar[str]
    CRYPT_AES_CTR: ClassVar[str]
    @overload
    def __init__(self, arg0: str, arg1: list[int]) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: list[int], arg2: int) -> None: ...
    def getName(self) -> str: ...
    def getKey(self) -> list[int]: ...
    def getTruncationLengthBits(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    @staticmethod
    def getSupportedAlgorithms() -> set: ...
    def toString(self) -> str: ...
