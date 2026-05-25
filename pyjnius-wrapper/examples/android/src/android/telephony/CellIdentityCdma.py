from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityCdma"]

class CellIdentityCdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityCdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNetworkId = JavaMethod("()I")
    getSystemId = JavaMethod("()I")
    getBasestationId = JavaMethod("()I")
    getLongitude = JavaMethod("()I")
    getLatitude = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")