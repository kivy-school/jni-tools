from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IccOpenLogicalChannelResponse"]

class IccOpenLogicalChannelResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/IccOpenLogicalChannelResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID_CHANNEL = JavaStaticField("I")
    STATUS_MISSING_RESOURCE = JavaStaticField("I")
    STATUS_NO_ERROR = JavaStaticField("I")
    STATUS_NO_SUCH_ELEMENT = JavaStaticField("I")
    STATUS_UNKNOWN_ERROR = JavaStaticField("I")
    getChannel = JavaMethod("()I")
    getStatus = JavaMethod("()I")
    getSelectResponse = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")