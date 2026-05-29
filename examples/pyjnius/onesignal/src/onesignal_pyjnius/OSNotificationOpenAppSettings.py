from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSNotificationOpenAppSettings"]

class OSNotificationOpenAppSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSNotificationOpenAppSettings"
    INSTANCE = JavaStaticField("Lcom/onesignal/OSNotificationOpenAppSettings;")
    getShouldOpenActivity = JavaMethod("(Landroid/content/Context;)Z")
    getSuppressLaunchURL = JavaMethod("(Landroid/content/Context;)Z")