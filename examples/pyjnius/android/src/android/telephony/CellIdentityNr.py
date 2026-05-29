from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityNr"]

class CellIdentityNr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityNr"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMncString = JavaMethod("()Ljava/lang/String;")
    getMccString = JavaMethod("()Ljava/lang/String;")
    getAdditionalPlmns = JavaMethod("()Ljava/util/Set;")
    getNrarfcn = JavaMethod("()I")
    getNci = JavaMethod("()J")
    getTac = JavaMethod("()I")
    getPci = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")