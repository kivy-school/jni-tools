from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityLte"]

class CellIdentityLte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityLte"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMcc = JavaMethod("()I")
    getMnc = JavaMethod("()I")
    getCi = JavaMethod("()I")
    getPci = JavaMethod("()I")
    getTac = JavaMethod("()I")
    getEarfcn = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    getBandwidth = JavaMethod("()I")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getClosedSubscriberGroupInfo = JavaMethod("()Landroid/telephony/ClosedSubscriberGroupInfo;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")