from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvAdManager"]

class TvAdManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/ad/TvAdManager"
    ACTION_APP_LINK_COMMAND = JavaStaticField("Ljava/lang/String;")
    APP_LINK_KEY_BACK_URI = JavaStaticField("Ljava/lang/String;")
    APP_LINK_KEY_CLASS_NAME = JavaStaticField("Ljava/lang/String;")
    APP_LINK_KEY_COMMAND_TYPE = JavaStaticField("Ljava/lang/String;")
    APP_LINK_KEY_PACKAGE_NAME = JavaStaticField("Ljava/lang/String;")
    APP_LINK_KEY_SERVICE_ID = JavaStaticField("Ljava/lang/String;")
    ERROR_BLOCKED = JavaStaticField("I")
    ERROR_ENCRYPTED = JavaStaticField("I")
    ERROR_NONE = JavaStaticField("I")
    ERROR_NOT_SUPPORTED = JavaStaticField("I")
    ERROR_RESOURCE_UNAVAILABLE = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    ERROR_UNKNOWN_CHANNEL = JavaStaticField("I")
    ERROR_WEAK_SIGNAL = JavaStaticField("I")
    INTENT_KEY_AD_SERVICE_ID = JavaStaticField("Ljava/lang/String;")
    INTENT_KEY_CHANNEL_URI = JavaStaticField("Ljava/lang/String;")
    INTENT_KEY_COMMAND_TYPE = JavaStaticField("Ljava/lang/String;")
    INTENT_KEY_TV_INPUT_ID = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_KEY_AD_BUFFER = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_KEY_AD_REQUEST = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_KEY_BROADCAST_INFO_REQUEST = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_KEY_REQUEST_ID = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_TYPE_AD_BUFFER_READY = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_TYPE_AD_REQUEST = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_TYPE_BROADCAST_INFO_REQUEST = JavaStaticField("Ljava/lang/String;")
    SESSION_DATA_TYPE_REMOVE_BROADCAST_INFO_REQUEST = JavaStaticField("Ljava/lang/String;")
    SESSION_STATE_ERROR = JavaStaticField("I")
    SESSION_STATE_RUNNING = JavaStaticField("I")
    SESSION_STATE_STOPPED = JavaStaticField("I")
    getTvAdServiceList = JavaMethod("()Ljava/util/List;")
    sendAppLinkCommand = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
    registerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/tv/ad/TvAdManager$TvAdServiceCallback;)V")
    unregisterCallback = JavaMethod("(Landroid/media/tv/ad/TvAdManager$TvAdServiceCallback;)V")

    class TvAdServiceCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/ad/TvAdManager$TvAdServiceCallback"
        __javaconstructor__ = [("()V", False)]
        onAdServiceAdded = JavaMethod("(Ljava/lang/String;)V")
        onAdServiceRemoved = JavaMethod("(Ljava/lang/String;)V")
        onAdServiceUpdated = JavaMethod("(Ljava/lang/String;)V")