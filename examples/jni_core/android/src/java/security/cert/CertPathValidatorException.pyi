from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable
from java.security.cert.CertPath import CertPath

class CertPathValidatorException:
    @overload
    def __init__(self, p0: str, p1: Throwable, p2: CertPath, p3: int, p4: Any) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable, p2: CertPath, p3: int) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    def getCertPath(self) -> CertPath: ...
    def getReason(self) -> Any: ...
    def getIndex(self) -> int: ...

    class BasicReason:
        UNSPECIFIED: ClassVar["BasicReason"]
        EXPIRED: ClassVar["BasicReason"]
        NOT_YET_VALID: ClassVar["BasicReason"]
        REVOKED: ClassVar["BasicReason"]
        UNDETERMINED_REVOCATION_STATUS: ClassVar["BasicReason"]
        INVALID_SIGNATURE: ClassVar["BasicReason"]
        ALGORITHM_CONSTRAINED: ClassVar["BasicReason"]
        UNSPECIFIED: ClassVar[Any]
        EXPIRED: ClassVar[Any]
        NOT_YET_VALID: ClassVar[Any]
        REVOKED: ClassVar[Any]
        UNDETERMINED_REVOCATION_STATUS: ClassVar[Any]
        INVALID_SIGNATURE: ClassVar[Any]
        ALGORITHM_CONSTRAINED: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Reason:
        ...
