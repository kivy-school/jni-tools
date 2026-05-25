from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HmsMessageServiceOneSignal"]

class HmsMessageServiceOneSignal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/HmsMessageServiceOneSignal"
    __javaconstructor__ = [("()V", False)]
    onNewToken = JavaMultipleMethod([("(Ljava/lang/String;Landroid/os/Bundle;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onMessageReceived = JavaMethod("(Lcom/huawei/hms/push/RemoteMessage;)V")