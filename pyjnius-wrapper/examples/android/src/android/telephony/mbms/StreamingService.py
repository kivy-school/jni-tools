from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamingService"]

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
    getPlaybackUri = JavaMethod("()Landroid/net/Uri;")
    getInfo = JavaMethod("()Landroid/telephony/mbms/StreamingServiceInfo;")
    close = JavaMethod("()V")