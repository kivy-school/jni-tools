from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSession2Service"]

class MediaSession2Service(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSession2Service"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onDestroy = JavaMethod("()V")
    onGetSession = JavaMethod("(Landroid/media/MediaSession2$ControllerInfo;)Landroid/media/MediaSession2;")
    onUpdateNotification = JavaMethod("(Landroid/media/MediaSession2;)Landroid/media/MediaSession2Service$MediaNotification;")
    addSession = JavaMethod("(Landroid/media/MediaSession2;)V")
    removeSession = JavaMethod("(Landroid/media/MediaSession2;)V")
    getSessions = JavaMethod("()Ljava/util/List;")

    class MediaNotification(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2Service/MediaNotification"
        __javaconstructor__ = [("(ILandroid/app/Notification;)V", False)]
        getNotificationId = JavaMethod("()I")
        getNotification = JavaMethod("()Landroid/app/Notification;")