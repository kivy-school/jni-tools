from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSessionManager"]

class MediaSessionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/session/MediaSessionManager"
    notifySession2Created = JavaMethod("(Landroid/media/Session2Token;)V")
    getActiveSessions = JavaMethod("(Landroid/content/ComponentName;)Ljava/util/List;")
    getMediaKeyEventSession = JavaMethod("()Landroid/media/session/MediaSession$Token;")
    getMediaKeyEventSessionPackageName = JavaMethod("()Ljava/lang/String;")
    getSession2Tokens = JavaMethod("()Ljava/util/List;")
    addOnActiveSessionsChangedListener = JavaMultipleMethod([("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;Landroid/content/ComponentName;)V", False, False), ("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;Landroid/content/ComponentName;Landroid/os/Handler;)V", False, False)])
    removeOnActiveSessionsChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;)V")
    addOnSession2TokensChangedListener = JavaMultipleMethod([("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;)V", False, False), ("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;Landroid/os/Handler;)V", False, False)])
    removeOnSession2TokensChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;)V")
    isTrustedForMediaControl = JavaMethod("(Landroid/media/session/MediaSessionManager$RemoteUserInfo;)Z")
    addOnMediaKeyEventSessionChangedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/session/MediaSessionManager$OnMediaKeyEventSessionChangedListener;)V")
    removeOnMediaKeyEventSessionChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnMediaKeyEventSessionChangedListener;)V")

    class OnActiveSessionsChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager/OnActiveSessionsChangedListener"
        onActiveSessionsChanged = JavaMethod("(Ljava/util/List;)V")

    class OnMediaKeyEventSessionChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager/OnMediaKeyEventSessionChangedListener"
        onMediaKeyEventSessionChanged = JavaMethod("(Ljava/lang/String;Landroid/media/session/MediaSession$Token;)V")

    class OnSession2TokensChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager/OnSession2TokensChangedListener"
        onSession2TokensChanged = JavaMethod("(Ljava/util/List;)V")

    class RemoteUserInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager/RemoteUserInfo"
        __javaconstructor__ = [("(Ljava/lang/String;II)V", False)]
        getPackageName = JavaMethod("()Ljava/lang/String;")
        getPid = JavaMethod("()I")
        getUid = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")