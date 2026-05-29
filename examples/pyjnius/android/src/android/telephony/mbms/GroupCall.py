from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GroupCall"]

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
    updateGroupCall = JavaMethod("(Ljava/util/List;Ljava/util/List;)V")
    getTmgi = JavaMethod("()J")
    close = JavaMethod("()V")