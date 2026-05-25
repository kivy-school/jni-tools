from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsRegistrationAttributes"]

class ImsRegistrationAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsRegistrationAttributes"
    ATTR_EPDG_OVER_CELL_INTERNET = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTransportType = JavaMethod("()I")
    getAttributeFlags = JavaMethod("()I")
    getFeatureTags = JavaMethod("()Ljava/util/Set;")
    getSipDetails = JavaMethod("()Landroid/telephony/ims/SipDetails;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")