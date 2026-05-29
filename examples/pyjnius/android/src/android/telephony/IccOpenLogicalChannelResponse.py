from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IccOpenLogicalChannelResponse"]

class IccOpenLogicalChannelResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/IccOpenLogicalChannelResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID_CHANNEL = JavaStaticField("I")
    STATUS_MISSING_RESOURCE = JavaStaticField("I")
    STATUS_NO_ERROR = JavaStaticField("I")
    STATUS_NO_SUCH_ELEMENT = JavaStaticField("I")
    STATUS_UNKNOWN_ERROR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getStatus = JavaMethod("()I")
    getSelectResponse = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    getChannel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")