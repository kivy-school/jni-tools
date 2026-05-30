from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DrmManagerClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmManagerClient"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    ERROR_NONE = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    acquireDrmInfo = JavaMethod("(Landroid/drm/DrmInfoRequest;)Landroid/drm/DrmInfo;")
    acquireRights = JavaMethod("(Landroid/drm/DrmInfoRequest;)I")
    canHandle = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Landroid/net/Uri;Ljava/lang/String;)Z", False, False)])
    checkRightsStatus = JavaMultipleMethod([("(Landroid/net/Uri;I)I", False, False), ("(Ljava/lang/String;I)I", False, False), ("(Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;)I", False, False)])
    closeConvertSession = JavaMethod("(I)Landroid/drm/DrmConvertedStatus;")
    convertData = JavaMethod("(I[B)Landroid/drm/DrmConvertedStatus;")
    getAvailableDrmEngines = JavaMethod("()[Ljava/lang/String;")
    getConstraints = JavaMultipleMethod([("(Landroid/net/Uri;I)Landroid/content/ContentValues;", False, False), ("(Ljava/lang/String;I)Landroid/content/ContentValues;", False, False)])
    getAvailableDrmSupportInfo = JavaMethod("()Ljava/util/Collection;")
    getDrmObjectType = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;)I", False, False)])
    getOriginalMimeType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Landroid/net/Uri;)Ljava/lang/String;", False, False)])
    openConvertSession = JavaMethod("(Ljava/lang/String;)I")
    processDrmInfo = JavaMethod("(Landroid/drm/DrmInfo;)I")
    removeAllRights = JavaMethod("()I")
    removeRights = JavaMultipleMethod([("(Landroid/net/Uri;)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    saveRights = JavaMethod("(Landroid/drm/DrmRights;Ljava/lang/String;Ljava/lang/String;)I")
    setOnEventListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnEventListener;)V")
    close = JavaMethod("()V")
    getMetadata = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/content/ContentValues;", False, False), ("(Ljava/lang/String;)Landroid/content/ContentValues;", False, False)])
    setOnErrorListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnErrorListener;)V")
    setOnInfoListener = JavaMethod("(Landroid/drm/DrmManagerClient$OnInfoListener;)V")
    release = JavaMethod("()V")

    class OnInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnInfoListener"
        onInfo = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmInfoEvent;)V")

    class OnEventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnEventListener"
        onEvent = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmEvent;)V")

    class OnErrorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmManagerClient$OnErrorListener"
        onError = JavaMethod("(Landroid/drm/DrmManagerClient;Landroid/drm/DrmErrorEvent;)V")

class ProcessedData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/ProcessedData"
    getAccountId = JavaMethod("()Ljava/lang/String;")
    getSubscriptionId = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()[B")

class DrmStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmStore"
    __javaconstructor__ = [("()V", False)]

    class RightsStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore$RightsStatus"
        __javaconstructor__ = [("()V", False)]
        RIGHTS_EXPIRED = JavaStaticField("I")
        RIGHTS_INVALID = JavaStaticField("I")
        RIGHTS_NOT_ACQUIRED = JavaStaticField("I")
        RIGHTS_VALID = JavaStaticField("I")

    class Playback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore$Playback"
        __javaconstructor__ = [("()V", False)]
        PAUSE = JavaStaticField("I")
        RESUME = JavaStaticField("I")
        START = JavaStaticField("I")
        STOP = JavaStaticField("I")

    class DrmObjectType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore$DrmObjectType"
        __javaconstructor__ = [("()V", False)]
        CONTENT = JavaStaticField("I")
        RIGHTS_OBJECT = JavaStaticField("I")
        TRIGGER_OBJECT = JavaStaticField("I")
        UNKNOWN = JavaStaticField("I")

    class ConstraintsColumns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore$ConstraintsColumns"
        EXTENDED_METADATA = JavaStaticField("Ljava/lang/String;")
        LICENSE_AVAILABLE_TIME = JavaStaticField("Ljava/lang/String;")
        LICENSE_EXPIRY_TIME = JavaStaticField("Ljava/lang/String;")
        LICENSE_START_TIME = JavaStaticField("Ljava/lang/String;")
        MAX_REPEAT_COUNT = JavaStaticField("Ljava/lang/String;")
        REMAINING_REPEAT_COUNT = JavaStaticField("Ljava/lang/String;")

    class Action(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmStore$Action"
        __javaconstructor__ = [("()V", False)]
        DEFAULT = JavaStaticField("I")
        DISPLAY = JavaStaticField("I")
        EXECUTE = JavaStaticField("I")
        OUTPUT = JavaStaticField("I")
        PLAY = JavaStaticField("I")
        PREVIEW = JavaStaticField("I")
        RINGTONE = JavaStaticField("I")
        TRANSFER = JavaStaticField("I")

class DrmInfoEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoEvent"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False), ("(IILjava/lang/String;Ljava/util/HashMap;)V", False)]
    TYPE_ACCOUNT_ALREADY_REGISTERED = JavaStaticField("I")
    TYPE_ALREADY_REGISTERED_BY_ANOTHER_ACCOUNT = JavaStaticField("I")
    TYPE_REMOVE_RIGHTS = JavaStaticField("I")
    TYPE_RIGHTS_INSTALLED = JavaStaticField("I")
    TYPE_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_WAIT_FOR_RIGHTS = JavaStaticField("I")
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")

class DrmUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmUtils"
    __javaconstructor__ = [("()V", False)]
    getExtendedMetadataParser = JavaStaticMethod("([B)Landroid/drm/DrmUtils$ExtendedMetadataParser;")

    class ExtendedMetadataParser(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/drm/DrmUtils$ExtendedMetadataParser"
        keyIterator = JavaMethod("()Ljava/util/Iterator;")
        get = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
        iterator = JavaMethod("()Ljava/util/Iterator;")

class DrmInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfo"
    __javaconstructor__ = [("(I[BLjava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;)V", False)]
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getInfoType = JavaMethod("()I")
    keyIterator = JavaMethod("()Ljava/util/Iterator;")
    getData = JavaMethod("()[B")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    iterator = JavaMethod("()Ljava/util/Iterator;")

class DrmRights(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmRights"
    __javaconstructor__ = [("(Landroid/drm/ProcessedData;Ljava/lang/String;)V", False), ("(Ljava/io/File;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getAccountId = JavaMethod("()Ljava/lang/String;")
    getSubscriptionId = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()[B")

class DrmInfoStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoStatus"
    __javaconstructor__ = [("(IILandroid/drm/ProcessedData;Ljava/lang/String;)V", False)]
    STATUS_ERROR = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    data = JavaField("Landroid/drm/ProcessedData;")
    infoType = JavaField("I")
    mimeType = JavaField("Ljava/lang/String;")
    statusCode = JavaField("I")

class DrmErrorEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmErrorEvent"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False), ("(IILjava/lang/String;Ljava/util/HashMap;)V", False)]
    TYPE_ACQUIRE_DRM_INFO_FAILED = JavaStaticField("I")
    TYPE_NOT_SUPPORTED = JavaStaticField("I")
    TYPE_NO_INTERNET_CONNECTION = JavaStaticField("I")
    TYPE_OUT_OF_MEMORY = JavaStaticField("I")
    TYPE_PROCESS_DRM_INFO_FAILED = JavaStaticField("I")
    TYPE_REMOVE_ALL_RIGHTS_FAILED = JavaStaticField("I")
    TYPE_RIGHTS_NOT_INSTALLED = JavaStaticField("I")
    TYPE_RIGHTS_RENEWAL_NOT_ALLOWED = JavaStaticField("I")
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")

class DrmEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmEvent"
    DRM_INFO_OBJECT = JavaStaticField("Ljava/lang/String;")
    DRM_INFO_STATUS_OBJECT = JavaStaticField("Ljava/lang/String;")
    TYPE_ALL_RIGHTS_REMOVED = JavaStaticField("I")
    TYPE_DRM_INFO_PROCESSED = JavaStaticField("I")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getUniqueId = JavaMethod("()I")

class DrmConvertedStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmConvertedStatus"
    __javaconstructor__ = [("(I[BI)V", False)]
    STATUS_ERROR = JavaStaticField("I")
    STATUS_INPUTDATA_ERROR = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    convertedData = JavaField("[B")
    offset = JavaField("I")
    statusCode = JavaField("I")

class DrmInfoRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfoRequest"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
    ACCOUNT_ID = JavaStaticField("Ljava/lang/String;")
    SUBSCRIPTION_ID = JavaStaticField("Ljava/lang/String;")
    TYPE_REGISTRATION_INFO = JavaStaticField("I")
    TYPE_RIGHTS_ACQUISITION_INFO = JavaStaticField("I")
    TYPE_RIGHTS_ACQUISITION_PROGRESS_INFO = JavaStaticField("I")
    TYPE_UNREGISTRATION_INFO = JavaStaticField("I")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getInfoType = JavaMethod("()I")
    keyIterator = JavaMethod("()Ljava/util/Iterator;")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    iterator = JavaMethod("()Ljava/util/Iterator;")

class DrmSupportInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmSupportInfo"
    __javaconstructor__ = [("()V", False)]
    addMimeType = JavaMethod("(Ljava/lang/String;)V")
    getDescriprition = JavaMethod("()Ljava/lang/String;")
    getFileSuffixIterator = JavaMethod("()Ljava/util/Iterator;")
    getMimeTypeIterator = JavaMethod("()Ljava/util/Iterator;")
    addFileSuffix = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getDescription = JavaMethod("()Ljava/lang/String;")