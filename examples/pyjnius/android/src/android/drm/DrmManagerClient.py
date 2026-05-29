from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmManagerClient"]

class DrmManagerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmManagerClient"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    ERROR_NONE = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    saveRights = JavaMethod("(Landroid/drm/DrmRights;Ljava/lang/String;Ljava/lang/String;)I")
    canHandle = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False)])
    getConstraints = JavaMultipleMethod([("(Landroid/net/Uri;I)Landroid/content/ContentValues;", False, False), ("(Ljava/lang/String;I)Landroid/content/ContentValues;", False, False)])
    checkRightsStatus = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;I)I", False, False), ("(Landroid/net/Uri;)I", False, False)])
    getDrmObjectType = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;)I", False, False)])
    convertData = JavaMethod("(I[B)Landroid/drm/DrmConvertedStatus;")
    acquireRights = JavaMethod("(Landroid/drm/DrmInfoRequest;)I")
    processDrmInfo = JavaMethod("(Landroid/drm/DrmInfo;)I")
    removeRights = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;)I", False, False)])
    openConvertSession = JavaMethod("(Ljava/lang/String;)I")
    removeAllRights = JavaMethod("()I")
    setOnEventListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnEventListener;)V")
    acquireDrmInfo = JavaMethod("(Landroid/drm/DrmInfoRequest;)Landroid/drm/DrmInfo;")
    closeConvertSession = JavaMethod("(I)Landroid/drm/DrmConvertedStatus;")
    getAvailableDrmEngines = JavaMethod("()[Ljava/lang/String;")
    getAvailableDrmSupportInfo = JavaMethod("()Ljava/util/Collection;")
    getOriginalMimeType = JavaMultipleMethod([("(Landroid/net/Uri;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    close = JavaMethod("()V")
    release = JavaMethod("()V")
    setOnErrorListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnErrorListener;)V")
    setOnInfoListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnInfoListener;)V")
    getMetadata = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/content/ContentValues;", False, False), ("(Ljava/lang/String;)Landroid/content/ContentValues;", False, False)])

    class OnInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnInfoListener"
        onInfo = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmInfoEvent;)V")

    class OnEventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnEventListener"
        onEvent = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmEvent;)V")

    class OnErrorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnErrorListener"
        onError = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmErrorEvent;)V")