from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipDetails"]

class SipDetails(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/SipDetails"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    METHOD_PUBLISH = JavaStaticField("I")
    METHOD_REGISTER = JavaStaticField("I")
    METHOD_SUBSCRIBE = JavaStaticField("I")
    METHOD_UNKNOWN = JavaStaticField("I")
    getMethod = JavaMethod("()I")
    getCSeq = JavaMethod("()I")
    getResponseCode = JavaMethod("()I")
    getResponsePhrase = JavaMethod("()Ljava/lang/String;")
    getReasonHeaderCause = JavaMethod("()I")
    getReasonHeaderText = JavaMethod("()Ljava/lang/String;")
    getCallId = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")