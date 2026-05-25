from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityTdscdma"]

class CellIdentityTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getCpid = JavaMethod("()I")
    getUarfcn = JavaMethod("()I")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getClosedSubscriberGroupInfo = JavaMethod("()Landroid/telephony/ClosedSubscriberGroupInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")