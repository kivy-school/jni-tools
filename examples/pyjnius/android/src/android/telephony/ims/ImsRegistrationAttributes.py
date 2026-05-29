from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsRegistrationAttributes"]

class ImsRegistrationAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsRegistrationAttributes"
    ATTR_EPDG_OVER_CELL_INTERNET = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSipDetails = JavaMethod("()Landroid/telephony/ims/SipDetails;")
    getFeatureTags = JavaMethod("()Ljava/util/Set;")
    getAttributeFlags = JavaMethod("()I")
    getTransportType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")