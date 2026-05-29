from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSessionManager"]

class MediaSessionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/session/MediaSessionManager"
    getSession2Tokens = JavaMethod("()Ljava/util/List;")
    getActiveSessions = JavaMethod("(Landroid/content/ComponentName;)Ljava/util/List;")
    addOnActiveSessionsChangedListener = JavaMultipleMethod([("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;Landroid/content/ComponentName;Landroid/os/Handler;)V", False, False), ("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;Landroid/content/ComponentName;)V", False, False)])
    addOnMediaKeyEventSessionChangedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/session/MediaSessionManager$OnMediaKeyEventSessionChangedListener;)V")
    addOnSession2TokensChangedListener = JavaMultipleMethod([("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;Landroid/os/Handler;)V", False, False), ("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;)V", False, False)])
    getMediaKeyEventSession = JavaMethod("()Landroid/media/session/MediaSession$Token;")
    getMediaKeyEventSessionPackageName = JavaMethod("()Ljava/lang/String;")
    isTrustedForMediaControl = JavaMethod("(Landroid/media/session/MediaSessionManager$RemoteUserInfo;)Z")
    notifySession2Created = JavaMethod("(Landroid/media/Session2Token;)V")
    removeOnActiveSessionsChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnActiveSessionsChangedListener;)V")
    removeOnMediaKeyEventSessionChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnMediaKeyEventSessionChangedListener;)V")
    removeOnSession2TokensChangedListener = JavaMethod("(Landroid/media/session/MediaSessionManager$OnSession2TokensChangedListener;)V")

    class RemoteUserInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager$RemoteUserInfo"
        __javaconstructor__ = [("(Ljava/lang/String;II)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getPackageName = JavaMethod("()Ljava/lang/String;")
        getPid = JavaMethod("()I")
        getUid = JavaMethod("()I")

    class OnSession2TokensChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager$OnSession2TokensChangedListener"
        onSession2TokensChanged = JavaMethod("(Ljava/util/List;)V")

    class OnMediaKeyEventSessionChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager$OnMediaKeyEventSessionChangedListener"
        onMediaKeyEventSessionChanged = JavaMethod("(Ljava/lang/String;Landroid/media/session/MediaSession$Token;)V")

    class OnActiveSessionsChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/session/MediaSessionManager$OnActiveSessionsChangedListener"
        onActiveSessionsChanged = JavaMethod("(Ljava/util/List;)V")