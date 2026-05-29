from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from java.lang.Throwable import Throwable

class ContentProviderResult:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    count: int
    exception: Throwable
    extras: Bundle
    uri: Uri
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self, p0: Bundle) -> None: ...
    @overload
    def __init__(self, p0: Uri) -> None: ...
    def toString(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
