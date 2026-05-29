from typing import Any, ClassVar, overload

class ParcelableSpan:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getSpanTypeId(self) -> int: ...
