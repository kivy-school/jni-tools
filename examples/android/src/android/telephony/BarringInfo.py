from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BarringInfo"]

class BarringInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/BarringInfo"
    BARRING_SERVICE_TYPE_CS_FALLBACK = JavaStaticField("I")
    BARRING_SERVICE_TYPE_CS_SERVICE = JavaStaticField("I")
    BARRING_SERVICE_TYPE_CS_VOICE = JavaStaticField("I")
    BARRING_SERVICE_TYPE_EMERGENCY = JavaStaticField("I")
    BARRING_SERVICE_TYPE_MMTEL_VIDEO = JavaStaticField("I")
    BARRING_SERVICE_TYPE_MMTEL_VOICE = JavaStaticField("I")
    BARRING_SERVICE_TYPE_MO_DATA = JavaStaticField("I")
    BARRING_SERVICE_TYPE_MO_SIGNALLING = JavaStaticField("I")
    BARRING_SERVICE_TYPE_PS_SERVICE = JavaStaticField("I")
    BARRING_SERVICE_TYPE_SMS = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBarringServiceInfo = JavaMethod("(I)Landroid/telephony/BarringInfo$BarringServiceInfo;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class BarringServiceInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/BarringInfo/BarringServiceInfo"
        BARRING_TYPE_CONDITIONAL = JavaStaticField("I")
        BARRING_TYPE_NONE = JavaStaticField("I")
        BARRING_TYPE_UNCONDITIONAL = JavaStaticField("I")
        BARRING_TYPE_UNKNOWN = JavaStaticField("I")
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getBarringType = JavaMethod("()I")
        isConditionallyBarred = JavaMethod("()Z")
        getConditionalBarringFactor = JavaMethod("()I")
        getConditionalBarringTimeSeconds = JavaMethod("()I")
        isBarred = JavaMethod("()Z")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")