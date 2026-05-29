from typing import Any, ClassVar, overload

class DOMException:
    INDEX_SIZE_ERR: ClassVar[int]
    DOMSTRING_SIZE_ERR: ClassVar[int]
    HIERARCHY_REQUEST_ERR: ClassVar[int]
    WRONG_DOCUMENT_ERR: ClassVar[int]
    INVALID_CHARACTER_ERR: ClassVar[int]
    NO_DATA_ALLOWED_ERR: ClassVar[int]
    NO_MODIFICATION_ALLOWED_ERR: ClassVar[int]
    NOT_FOUND_ERR: ClassVar[int]
    NOT_SUPPORTED_ERR: ClassVar[int]
    INUSE_ATTRIBUTE_ERR: ClassVar[int]
    INVALID_STATE_ERR: ClassVar[int]
    SYNTAX_ERR: ClassVar[int]
    INVALID_MODIFICATION_ERR: ClassVar[int]
    NAMESPACE_ERR: ClassVar[int]
    INVALID_ACCESS_ERR: ClassVar[int]
    VALIDATION_ERR: ClassVar[int]
    TYPE_MISMATCH_ERR: ClassVar[int]
    code: int
    def __init__(self, p0: int, p1: str) -> None: ...
