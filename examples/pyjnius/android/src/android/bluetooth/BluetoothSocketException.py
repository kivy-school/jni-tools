from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothSocketException"]

class BluetoothSocketException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothSocketException"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/lang/String;)V", False)]
    BLUETOOTH_OFF_FAILURE = JavaStaticField("I")
    L2CAP_ACL_FAILURE = JavaStaticField("I")
    L2CAP_CLIENT_SECURITY_FAILURE = JavaStaticField("I")
    L2CAP_INSUFFICIENT_AUTHENTICATION = JavaStaticField("I")
    L2CAP_INSUFFICIENT_AUTHORIZATION = JavaStaticField("I")
    L2CAP_INSUFFICIENT_ENCRYPTION = JavaStaticField("I")
    L2CAP_INSUFFICIENT_ENCRYPT_KEY_SIZE = JavaStaticField("I")
    L2CAP_INVALID_PARAMETERS = JavaStaticField("I")
    L2CAP_INVALID_SOURCE_CID = JavaStaticField("I")
    L2CAP_NO_PSM_AVAILABLE = JavaStaticField("I")
    L2CAP_NO_RESOURCES = JavaStaticField("I")
    L2CAP_SOURCE_CID_ALREADY_ALLOCATED = JavaStaticField("I")
    L2CAP_TIMEOUT = JavaStaticField("I")
    L2CAP_UNACCEPTABLE_PARAMETERS = JavaStaticField("I")
    L2CAP_UNKNOWN = JavaStaticField("I")
    NULL_DEVICE = JavaStaticField("I")
    RPC_FAILURE = JavaStaticField("I")
    SOCKET_CLOSED = JavaStaticField("I")
    SOCKET_CONNECTION_FAILURE = JavaStaticField("I")
    SOCKET_MANAGER_FAILURE = JavaStaticField("I")
    UNIX_FILE_SOCKET_CREATION_FAILURE = JavaStaticField("I")
    UNSPECIFIED = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")