from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSession2"]

class MediaSession2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSession2"
    broadcastSessionCommand = JavaMethod("(Landroid/media/Session2Command;Landroid/os/Bundle;)V")
    isPlaybackActive = JavaMethod("()Z")
    cancelSessionCommand = JavaMethod("(Landroid/media/MediaSession2$ControllerInfo;Ljava/lang/Object;)V")
    getConnectedControllers = JavaMethod("()Ljava/util/List;")
    sendSessionCommand = JavaMethod("(Landroid/media/MediaSession2$ControllerInfo;Landroid/media/Session2Command;Landroid/os/Bundle;)Ljava/lang/Object;")
    setPlaybackActive = JavaMethod("(Z)V")
    close = JavaMethod("()V")
    getId = JavaMethod("()Ljava/lang/String;")
    getToken = JavaMethod("()Landroid/media/Session2Token;")

    class SessionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2$SessionCallback"
        __javaconstructor__ = [("()V", False)]
        onDisconnected = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)V")
        onCommandResult = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;Ljava/lang/Object;Landroid/media/Session2Command;Landroid/media/Session2Command$Result;)V")
        onConnect = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)Landroid/media/Session2CommandGroup;")
        onSessionCommand = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;Landroid/media/Session2Command;Landroid/os/Bundle;)Landroid/media/Session2Command$Result;")
        onPostConnect = JavaMethod("(Landroid/media/MediaSession2;Landroid/media/MediaSession2$ControllerInfo;)V")

    class ControllerInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2$ControllerInfo"
        getConnectionHints = JavaMethod("()Landroid/os/Bundle;")
        getRemoteUserInfo = JavaMethod("()Landroid/media/session/MediaSessionManager$RemoteUserInfo;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getPackageName = JavaMethod("()Ljava/lang/String;")
        getUid = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSession2$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setSessionActivity = JavaMethod("(Landroid/app/PendingIntent;)Landroid/media/MediaSession2$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/media/MediaSession2$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/media/MediaSession2$Builder;")
        setSessionCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaSession2$SessionCallback;)Landroid/media/MediaSession2$Builder;")
        build = JavaMethod("()Landroid/media/MediaSession2;")