from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityWcdma"]

class CellIdentityWcdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityWcdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMcc = JavaMethod("()I")
    getMnc = JavaMethod("()I")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getPsc = JavaMethod("()I")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUarfcn = JavaMethod("()I")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getClosedSubscriberGroupInfo = JavaMethod("()Landroid/telephony/ClosedSubscriberGroupInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")