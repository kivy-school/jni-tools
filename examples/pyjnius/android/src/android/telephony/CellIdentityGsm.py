from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityGsm"]

class CellIdentityGsm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityGsm"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMcc = JavaMethod("()I")
    getMnc = JavaMethod("()I")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getArfcn = JavaMethod("()I")
    getBsic = JavaMethod("()I")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getPsc = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")