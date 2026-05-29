from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityLte"]

class CellIdentityLte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityLte"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMcc = JavaMethod("()I")
    getMnc = JavaMethod("()I")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMobileNetworkOperator = JavaMethod("()Ljava/lang/String;")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getClosedSubscriberGroupInfo = JavaMethod("()Landroid/telephony/ClosedSubscriberGroupInfo;")
    getEarfcn = JavaMethod("()I")
    getBandwidth = JavaMethod("()I")
    getTac = JavaMethod("()I")
    getPci = JavaMethod("()I")
    getCi = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")