from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisconnectCause"]

class DisconnectCause(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/DisconnectCause"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/CharSequence;Ljava/lang/CharSequence;Ljava/lang/String;I)V", False), ("(ILjava/lang/CharSequence;Ljava/lang/CharSequence;Ljava/lang/String;)V", False), ("(I)V", False)]
    ANSWERED_ELSEWHERE = JavaStaticField("I")
    BUSY = JavaStaticField("I")
    CALL_PULLED = JavaStaticField("I")
    CANCELED = JavaStaticField("I")
    CONNECTION_MANAGER_NOT_SUPPORTED = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ERROR = JavaStaticField("I")
    LOCAL = JavaStaticField("I")
    MISSED = JavaStaticField("I")
    OTHER = JavaStaticField("I")
    REASON_EMERGENCY_CALL_PLACED = JavaStaticField("Ljava/lang/String;")
    REASON_EMULATING_SINGLE_CALL = JavaStaticField("Ljava/lang/String;")
    REASON_IMS_ACCESS_BLOCKED = JavaStaticField("Ljava/lang/String;")
    REASON_WIFI_ON_BUT_WFC_OFF = JavaStaticField("Ljava/lang/String;")
    REJECTED = JavaStaticField("I")
    REMOTE = JavaStaticField("I")
    RESTRICTED = JavaStaticField("I")
    UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTone = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCode = JavaMethod("()I")
    getReason = JavaMethod("()Ljava/lang/String;")