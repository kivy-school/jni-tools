from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityTdscdma"]

class CellIdentityTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    getUarfcn = JavaMethod("()I")
    getCpid = JavaMethod("()I")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getLac = JavaMethod("()I")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getCid = JavaMethod("()I")
    getClosedSubscriberGroupInfo = JavaMethod("()Landroid/telephony/ClosedSubscriberGroupInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")