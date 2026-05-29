from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SetValueResult:
    CREATOR: ClassVar[Any]
    RESULT_DISABLED: ClassVar[int]
    RESULT_DISALLOW: ClassVar[int]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_INVALID_REQUEST: ClassVar[int]
    RESULT_OK: ClassVar[int]
    RESULT_REQUIRE_APP_PERMISSION: ClassVar[int]
    RESULT_REQUIRE_USER_CONSENT: ClassVar[int]
    RESULT_RESTRICTED: ClassVar[int]
    RESULT_UNAVAILABLE: ClassVar[int]
    RESULT_UNSUPPORTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def build(self) -> "SetValueResult": ...
