from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalHmsEventBridge"]

class OneSignalHmsEventBridge(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalHmsEventBridge"
    __javaconstructor__ = [("()V", False)]
    HMS_TTL_KEY = JavaStaticField("Ljava/lang/String;")
    HMS_SENT_TIME_KEY = JavaStaticField("Ljava/lang/String;")
    onNewToken = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;)V", True, False), ("(Landroid/content/Context;Ljava/lang/String;)V", True, False)])
    onMessageReceived = JavaStaticMethod("(Landroid/content/Context;Lcom/huawei/hms/push/RemoteMessage;)V")