from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OneSignalNotificationManager"]

class OneSignalNotificationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OneSignalNotificationManager"
    __javaconstructor__ = [("()V", False)]
    areNotificationsEnabled = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Z")