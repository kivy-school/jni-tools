from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportHandle"]

class TransportHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/TransportHandle"
    registerReceiveCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/ranging/oob/TransportHandle$ReceiveCallback;)V")
    sendData = JavaMethod("([B)V")

    class ReceiveCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/TransportHandle$ReceiveCallback"
        onReceiveData = JavaMethod("([B)V")
        onDisconnect = JavaMethod("()V")
        onReconnect = JavaMethod("()V")
        onSendFailed = JavaMethod("()V")
        onClose = JavaMethod("()V")