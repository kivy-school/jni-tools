from typing import Any, ClassVar, overload

class BluetoothSocketException:
    BLUETOOTH_OFF_FAILURE: ClassVar[int]
    L2CAP_ACL_FAILURE: ClassVar[int]
    L2CAP_CLIENT_SECURITY_FAILURE: ClassVar[int]
    L2CAP_INSUFFICIENT_AUTHENTICATION: ClassVar[int]
    L2CAP_INSUFFICIENT_AUTHORIZATION: ClassVar[int]
    L2CAP_INSUFFICIENT_ENCRYPTION: ClassVar[int]
    L2CAP_INSUFFICIENT_ENCRYPT_KEY_SIZE: ClassVar[int]
    L2CAP_INVALID_PARAMETERS: ClassVar[int]
    L2CAP_INVALID_SOURCE_CID: ClassVar[int]
    L2CAP_NO_PSM_AVAILABLE: ClassVar[int]
    L2CAP_NO_RESOURCES: ClassVar[int]
    L2CAP_SOURCE_CID_ALREADY_ALLOCATED: ClassVar[int]
    L2CAP_TIMEOUT: ClassVar[int]
    L2CAP_UNACCEPTABLE_PARAMETERS: ClassVar[int]
    L2CAP_UNKNOWN: ClassVar[int]
    NULL_DEVICE: ClassVar[int]
    RPC_FAILURE: ClassVar[int]
    SOCKET_CLOSED: ClassVar[int]
    SOCKET_CONNECTION_FAILURE: ClassVar[int]
    SOCKET_MANAGER_FAILURE: ClassVar[int]
    UNIX_FILE_SOCKET_CREATION_FAILURE: ClassVar[int]
    UNSPECIFIED: ClassVar[int]
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
    def getErrorCode(self) -> int: ...
