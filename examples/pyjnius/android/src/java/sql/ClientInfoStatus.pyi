from typing import Any, ClassVar, overload

class ClientInfoStatus:
    REASON_UNKNOWN: ClassVar["ClientInfoStatus"]
    REASON_UNKNOWN_PROPERTY: ClassVar["ClientInfoStatus"]
    REASON_VALUE_INVALID: ClassVar["ClientInfoStatus"]
    REASON_VALUE_TRUNCATED: ClassVar["ClientInfoStatus"]
    REASON_UNKNOWN: ClassVar["ClientInfoStatus"]
    REASON_UNKNOWN_PROPERTY: ClassVar["ClientInfoStatus"]
    REASON_VALUE_INVALID: ClassVar["ClientInfoStatus"]
    REASON_VALUE_TRUNCATED: ClassVar["ClientInfoStatus"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ClientInfoStatus": ...
