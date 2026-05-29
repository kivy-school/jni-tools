from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBarringServiceInfo = JavaMethod("(I)Landroid/telephony/BarringInfo$BarringServiceInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class BarringServiceInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/BarringInfo$BarringServiceInfo"
        BARRING_TYPE_CONDITIONAL = JavaStaticField("I")
        BARRING_TYPE_NONE = JavaStaticField("I")
        BARRING_TYPE_UNCONDITIONAL = JavaStaticField("I")
        BARRING_TYPE_UNKNOWN = JavaStaticField("I")
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getConditionalBarringTimeSeconds = JavaMethod("()I")
        isConditionallyBarred = JavaMethod("()Z")
        getConditionalBarringFactor = JavaMethod("()I")
        isBarred = JavaMethod("()Z")
        getBarringType = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")