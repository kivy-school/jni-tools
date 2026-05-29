from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipDetails"]

class SipDetails(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/SipDetails"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    METHOD_PUBLISH = JavaStaticField("I")
    METHOD_REGISTER = JavaStaticField("I")
    METHOD_SUBSCRIBE = JavaStaticField("I")
    METHOD_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCSeq = JavaMethod("()I")
    getCallId = JavaMethod("()Ljava/lang/String;")
    getReasonHeaderCause = JavaMethod("()I")
    getReasonHeaderText = JavaMethod("()Ljava/lang/String;")
    getResponsePhrase = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMethod = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getResponseCode = JavaMethod("()I")