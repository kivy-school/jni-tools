from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityNr"]

class CellIdentityNr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityNr"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getNci = JavaMethod("()J")
    getNrarfcn = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    getPci = JavaMethod("()I")
    getTac = JavaMethod("()I")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")