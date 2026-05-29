from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketKeepalive"]

class SocketKeepalive(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/SocketKeepalive"
    ERROR_HARDWARE_ERROR = JavaStaticField("I")
    ERROR_INSUFFICIENT_RESOURCES = JavaStaticField("I")
    ERROR_INVALID_INTERVAL = JavaStaticField("I")
    ERROR_INVALID_IP_ADDRESS = JavaStaticField("I")
    ERROR_INVALID_LENGTH = JavaStaticField("I")
    ERROR_INVALID_NETWORK = JavaStaticField("I")
    ERROR_INVALID_PORT = JavaStaticField("I")
    ERROR_INVALID_SOCKET = JavaStaticField("I")
    ERROR_SOCKET_NOT_IDLE = JavaStaticField("I")
    ERROR_UNSUPPORTED = JavaStaticField("I")
    close = JavaMethod("()V")
    start = JavaMethod("(I)V")
    stop = JavaMethod("()V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/SocketKeepalive$Callback"
        __javaconstructor__ = [("()V", False)]
        onDataReceived = JavaMethod("()V")
        onError = JavaMethod("(I)V")
        onStarted = JavaMethod("()V")
        onStopped = JavaMethod("()V")