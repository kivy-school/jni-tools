from typing import Any, ClassVar, overload

class InvalidMajorVersionException:
    ERROR_TYPE_AUTHENTICATION_FAILED: ClassVar[int]
    ERROR_TYPE_CHILD_SA_NOT_FOUND: ClassVar[int]
    ERROR_TYPE_FAILED_CP_REQUIRED: ClassVar[int]
    ERROR_TYPE_INTERNAL_ADDRESS_FAILURE: ClassVar[int]
    ERROR_TYPE_INVALID_IKE_SPI: ClassVar[int]
    ERROR_TYPE_INVALID_KE_PAYLOAD: ClassVar[int]
    ERROR_TYPE_INVALID_MAJOR_VERSION: ClassVar[int]
    ERROR_TYPE_INVALID_MESSAGE_ID: ClassVar[int]
    ERROR_TYPE_INVALID_SELECTORS: ClassVar[int]
    ERROR_TYPE_INVALID_SYNTAX: ClassVar[int]
    ERROR_TYPE_NO_ADDITIONAL_SAS: ClassVar[int]
    ERROR_TYPE_NO_PROPOSAL_CHOSEN: ClassVar[int]
    ERROR_TYPE_SINGLE_PAIR_REQUIRED: ClassVar[int]
    ERROR_TYPE_TEMPORARY_FAILURE: ClassVar[int]
    ERROR_TYPE_TS_UNACCEPTABLE: ClassVar[int]
    ERROR_TYPE_UNSUPPORTED_CRITICAL_PAYLOAD: ClassVar[int]
    def __init__(self, p0: int) -> None: ...
    def getMajorVersion(self) -> int: ...
