from typing import Any, ClassVar, overload

class PKIXReason:
    NAME_CHAINING: ClassVar["PKIXReason"]
    INVALID_KEY_USAGE: ClassVar["PKIXReason"]
    INVALID_POLICY: ClassVar["PKIXReason"]
    NO_TRUST_ANCHOR: ClassVar["PKIXReason"]
    UNRECOGNIZED_CRIT_EXT: ClassVar["PKIXReason"]
    NOT_CA_CERT: ClassVar["PKIXReason"]
    PATH_TOO_LONG: ClassVar["PKIXReason"]
    INVALID_NAME: ClassVar["PKIXReason"]
    @staticmethod
    def values() -> list["PKIXReason"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "PKIXReason": ...
