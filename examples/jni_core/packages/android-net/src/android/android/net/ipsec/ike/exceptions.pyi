from typing import Any, ClassVar, overload

class IkeNonProtocolException:
    ...

from typing import Any, ClassVar, overload

class InvalidSelectorsException:
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
    def __init__(self, p0: int, p1: Any) -> None: ...
    def getIpSecPacketInfo(self) -> Any: ...
    def getIpSecSpi(self) -> int: ...

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

from typing import Any, ClassVar, overload

class IkeTimeoutException:
    def __init__(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload

class IkeProtocolException:
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
    def getErrorType(self) -> int: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class IkeInternalException:
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...

from typing import Any, ClassVar, overload
from android.net.Network import Network

class IkeNetworkLostException:
    def __init__(self, p0: Network) -> None: ...
    def getNetwork(self) -> Network: ...

from typing import Any, ClassVar, overload

class InvalidKeException:
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
    def getDhGroup(self) -> int: ...

from typing import Any, ClassVar, overload

class IkeException:
    ...

from typing import Any, ClassVar, overload
from java.io.IOException import IOException
from java.lang.Throwable import Throwable

class IkeIOException:
    def __init__(self, p0: IOException) -> None: ...
    @overload
    def getCause(self) -> Throwable: ...
    @overload
    def getCause(self) -> IOException: ...
    def initCause(self, p0: Throwable) -> Throwable: ...

