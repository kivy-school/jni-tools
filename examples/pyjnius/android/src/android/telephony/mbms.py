from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FileServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/FileServiceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getFiles = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class MbmsDownloadReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsDownloadReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")

class MbmsStreamingSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsStreamingSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onMiddlewareReady = JavaMethod("()V")
    onStreamingServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onError = JavaMethod("(ILjava/lang/String;)V")

class MbmsDownloadSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsDownloadSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onMiddlewareReady = JavaMethod("()V")
    onFileServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onError = JavaMethod("(ILjava/lang/String;)V")

class FileInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/FileInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class StreamingServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingServiceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class GroupCallCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/GroupCallCallback"
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")
    onGroupCallStateChanged = JavaMethod("(II)V")
    onError = JavaMethod("(ILjava/lang/String;)V")

class DownloadProgressListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadProgressListener"
    __javaconstructor__ = [("()V", False)]
    onProgressUpdated = JavaMethod("(Landroid/telephony/mbms/DownloadRequest;Landroid/telephony/mbms/FileInfo;IIII)V")

class MbmsErrors(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsErrors"
    ERROR_MIDDLEWARE_LOST = JavaStaticField("I")
    ERROR_MIDDLEWARE_NOT_BOUND = JavaStaticField("I")
    ERROR_NO_UNIQUE_MIDDLEWARE = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    UNKNOWN = JavaStaticField("I")

    class StreamingErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$StreamingErrors"
        ERROR_CONCURRENT_SERVICE_LIMIT_REACHED = JavaStaticField("I")
        ERROR_DUPLICATE_START_STREAM = JavaStaticField("I")
        ERROR_UNABLE_TO_START_SERVICE = JavaStaticField("I")

    class InitializationErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$InitializationErrors"
        ERROR_APP_PERMISSIONS_NOT_GRANTED = JavaStaticField("I")
        ERROR_DUPLICATE_INITIALIZE = JavaStaticField("I")
        ERROR_UNABLE_TO_INITIALIZE = JavaStaticField("I")

    class GroupCallErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$GroupCallErrors"
        ERROR_DUPLICATE_START_GROUP_CALL = JavaStaticField("I")
        ERROR_UNABLE_TO_START_SERVICE = JavaStaticField("I")

    class GeneralErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$GeneralErrors"
        ERROR_CARRIER_CHANGE_NOT_ALLOWED = JavaStaticField("I")
        ERROR_IN_E911 = JavaStaticField("I")
        ERROR_MIDDLEWARE_NOT_YET_READY = JavaStaticField("I")
        ERROR_MIDDLEWARE_TEMPORARILY_UNAVAILABLE = JavaStaticField("I")
        ERROR_NOT_CONNECTED_TO_HOME_CARRIER_LTE = JavaStaticField("I")
        ERROR_OUT_OF_MEMORY = JavaStaticField("I")
        ERROR_UNABLE_TO_READ_SIM = JavaStaticField("I")

    class DownloadErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$DownloadErrors"
        ERROR_CANNOT_CHANGE_TEMP_FILE_ROOT = JavaStaticField("I")
        ERROR_MALFORMED_SERVICE_ANNOUNCEMENT = JavaStaticField("I")
        ERROR_UNKNOWN_DOWNLOAD_REQUEST = JavaStaticField("I")
        ERROR_UNKNOWN_FILE_INFO = JavaStaticField("I")

class StreamingService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingService"
    BROADCAST_METHOD = JavaStaticField("I")
    REASON_BY_USER_REQUEST = JavaStaticField("I")
    REASON_END_OF_SESSION = JavaStaticField("I")
    REASON_FREQUENCY_CONFLICT = JavaStaticField("I")
    REASON_LEFT_MBMS_BROADCAST_AREA = JavaStaticField("I")
    REASON_NONE = JavaStaticField("I")
    REASON_NOT_CONNECTED_TO_HOMECARRIER_LTE = JavaStaticField("I")
    REASON_OUT_OF_MEMORY = JavaStaticField("I")
    STATE_STALLED = JavaStaticField("I")
    STATE_STARTED = JavaStaticField("I")
    STATE_STOPPED = JavaStaticField("I")
    UNICAST_METHOD = JavaStaticField("I")
    getInfo = JavaMethod("()Landroid/telephony/mbms/StreamingServiceInfo;")
    getPlaybackUri = JavaMethod("()Landroid/net/Uri;")
    close = JavaMethod("()V")

class MbmsGroupCallSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsGroupCallSessionCallback"
    onAvailableSaisUpdated = JavaMethod("(Ljava/util/List;Ljava/util/List;)V")
    onServiceInterfaceAvailable = JavaMethod("(Ljava/lang/String;I)V")
    onMiddlewareReady = JavaMethod("()V")
    onError = JavaMethod("(ILjava/lang/String;)V")

class StreamingServiceCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingServiceCallback"
    __javaconstructor__ = [("()V", False)]
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")
    onStreamStateUpdated = JavaMethod("(II)V")
    onMediaDescriptionUpdated = JavaMethod("()V")
    onStreamMethodUpdated = JavaMethod("(I)V")
    onError = JavaMethod("(ILjava/lang/String;)V")

class DownloadStatusListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadStatusListener"
    __javaconstructor__ = [("()V", False)]
    onStatusUpdated = JavaMethod("(Landroid/telephony/mbms/DownloadRequest;Landroid/telephony/mbms/FileInfo;I)V")

class GroupCall(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/GroupCall"
    REASON_BY_USER_REQUEST = JavaStaticField("I")
    REASON_FREQUENCY_CONFLICT = JavaStaticField("I")
    REASON_LEFT_MBMS_BROADCAST_AREA = JavaStaticField("I")
    REASON_NONE = JavaStaticField("I")
    REASON_NOT_CONNECTED_TO_HOMECARRIER_LTE = JavaStaticField("I")
    REASON_OUT_OF_MEMORY = JavaStaticField("I")
    STATE_STALLED = JavaStaticField("I")
    STATE_STARTED = JavaStaticField("I")
    STATE_STOPPED = JavaStaticField("I")
    getTmgi = JavaMethod("()J")
    updateGroupCall = JavaMethod("(Ljava/util/List;Ljava/util/List;)V")
    close = JavaMethod("()V")

class DownloadRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSubscriptionId = JavaMethod("()I")
    getFileServiceId = JavaMethod("()Ljava/lang/String;")
    getMaxAppIntentSize = JavaStaticMethod("()I")
    getDestinationUri = JavaMethod("()Landroid/net/Uri;")
    getSourceUri = JavaMethod("()Landroid/net/Uri;")
    getMaxDestinationUriSize = JavaStaticMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toByteArray = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/DownloadRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Landroid/net/Uri;)V", False)]
        setAppIntent = JavaMethod("(Landroid/content/Intent;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setServiceInfo = JavaMethod("(Landroid/telephony/mbms/FileServiceInfo;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        fromDownloadRequest = JavaStaticMethod("(Landroid/telephony/mbms/DownloadRequest;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        fromSerializedRequest = JavaStaticMethod("([B)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setSubscriptionId = JavaMethod("(I)Landroid/telephony/mbms/DownloadRequest$Builder;")
        build = JavaMethod("()Landroid/telephony/mbms/DownloadRequest;")

class ServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/ServiceInfo"
    getNameForLocale = JavaMethod("(Ljava/util/Locale;)Ljava/lang/CharSequence;")
    getNamedContentLocales = JavaMethod("()Ljava/util/Set;")
    getServiceClassName = JavaMethod("()Ljava/lang/String;")
    getServiceId = JavaMethod("()Ljava/lang/String;")
    getSessionEndTime = JavaMethod("()Ljava/util/Date;")
    getSessionStartTime = JavaMethod("()Ljava/util/Date;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLocales = JavaMethod("()Ljava/util/List;")