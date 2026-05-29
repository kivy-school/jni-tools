from typing import Any, ClassVar, overload

class StringPrepParseException:
    ACE_PREFIX_ERROR: ClassVar[int]
    BUFFER_OVERFLOW_ERROR: ClassVar[int]
    CHECK_BIDI_ERROR: ClassVar[int]
    DOMAIN_NAME_TOO_LONG_ERROR: ClassVar[int]
    ILLEGAL_CHAR_FOUND: ClassVar[int]
    INVALID_CHAR_FOUND: ClassVar[int]
    LABEL_TOO_LONG_ERROR: ClassVar[int]
    PROHIBITED_ERROR: ClassVar[int]
    STD3_ASCII_RULES_ERROR: ClassVar[int]
    UNASSIGNED_ERROR: ClassVar[int]
    VERIFICATION_ERROR: ClassVar[int]
    ZERO_LENGTH_LABEL: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: int, p2: str, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int, p2: str, p3: int) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getError(self) -> int: ...
