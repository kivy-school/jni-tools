from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSMutableNotification"]

class OSMutableNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSMutableNotification"
    setExtender = JavaMethod("(Landroidx/core/app/NotificationCompat$Extender;)V")
    setAndroidNotificationId = JavaMethod("(I)V")