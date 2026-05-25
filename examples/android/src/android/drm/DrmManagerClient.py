from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmManagerClient"]

class DrmManagerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmManagerClient"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    ERROR_NONE = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    finalize = JavaMethod("()V")
    close = JavaMethod("()V")
    release = JavaMethod("()V")
    setOnInfoListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnInfoListener;)V")
    setOnEventListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnEventListener;)V")
    setOnErrorListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnErrorListener;)V")
    getAvailableDrmEngines = JavaMethod("()[Ljava/lang/String;")
    getAvailableDrmSupportInfo = JavaMethod("()Ljava/util/Collection;")
    getConstraints = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/content/ContentValues;", False, False), ("(Landroid/net/Uri;I)Landroid/content/ContentValues;", False, False)])
    getMetadata = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/content/ContentValues;", False, False), ("(Landroid/net/Uri;)Landroid/content/ContentValues;", False, False)])
    saveRights = JavaMethod("(Landroid/drm/DrmRights;Ljava/lang/String;Ljava/lang/String;)I")
    canHandle = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Landroid/net/Uri;Ljava/lang/String;)Z", False, False)])
    processDrmInfo = JavaMethod("(Landroid/drm/DrmInfo;)I")
    acquireDrmInfo = JavaMethod("(Landroid/drm/DrmInfoRequest;)Landroid/drm/DrmInfo;")
    acquireRights = JavaMethod("(Landroid/drm/DrmInfoRequest;)I")
    getDrmObjectType = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Ljava/lang/String;)I", False, False)])
    getOriginalMimeType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Landroid/net/Uri;)Ljava/lang/String;", False, False)])
    checkRightsStatus = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;)I", False, False), ("(Ljava/lang/String;I)I", False, False), ("(Landroid/net/Uri;I)I", False, False)])
    removeRights = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;)I", False, False)])
    removeAllRights = JavaMethod("()I")
    openConvertSession = JavaMethod("(Ljava/lang/String;)I")
    convertData = JavaMethod("(I[B)Landroid/drm/DrmConvertedStatus;")
    closeConvertSession = JavaMethod("(I)Landroid/drm/DrmConvertedStatus;")

    class OnErrorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient/OnErrorListener"
        onError = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmErrorEvent;)V")

    class OnEventListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient/OnEventListener"
        onEvent = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmEvent;)V")

    class OnInfoListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient/OnInfoListener"
        onInfo = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmInfoEvent;)V")