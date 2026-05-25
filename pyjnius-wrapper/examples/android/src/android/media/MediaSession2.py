from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSession2"]

class MediaSession2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSession2"
    close = JavaMethod("()V")
    getId = JavaMethod("()Ljava/lang/String;")
    getToken = JavaMethod("()Landroid/media/Session2Token;")
    broadcastSessionCommand = JavaMethod("(Landroid/media/Session2Command;Landroid/os/Bundle;)V")
    sendSessionCommand = JavaMethod("(Landroid/media/MediaSession2$ControllerInfo;Landroid/media/Session2Command;Landroid/os/Bundle;)Ljava/lang/Object;")
    cancelSessionCommand = JavaMethod("(Landroid/media/MediaSession2$ControllerInfo;Ljava/lang/Object;)V")
    setPlaybackActive = JavaMethod("(Z)V")
    isPlaybackActive = JavaMethod("()Z")
    getConnectedControllers = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setSessionActivity = JavaMethod("(Landroid/app/PendingIntent;)Landroid/media/MediaSession2$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/media/MediaSession2$Builder;")
        setSessionCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaSession2$SessionCallback;)Landroid/media/MediaSession2$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/media/MediaSession2$Builder;")
        build = JavaMethod("()Landroid/media/MediaSession2;")

    class ControllerInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2/ControllerInfo"
        getRemoteUserInfo = JavaMethod("()Landroid/media/session/MediaSessionManager$RemoteUserInfo;")
        getPackageName = JavaMethod("()Ljava/lang/String;")
        getUid = JavaMethod("()I")
        getConnectionHints = JavaMethod("()Landroid/os/Bundle;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")

    class SessionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2/SessionCallback"
        __javaconstructor__ = [("()V", False)]
        onConnect = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)Landroid/media/Session2CommandGroup;")
        onPostConnect = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)V")
        onDisconnected = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)V")
        onSessionCommand = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;Landroid/media/Session2Command;Landroid/os/Bundle;)Landroid/media/Session2Command$Result;")
        onCommandResult = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;Ljava/lang/Object;Landroid/media/Session2Command;Landroid/media/Session2Command$Result;)V")