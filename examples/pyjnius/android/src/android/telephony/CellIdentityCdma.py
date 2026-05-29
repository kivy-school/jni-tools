from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentityCdma"]

class CellIdentityCdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentityCdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSystemId = JavaMethod("()I")
    getBasestationId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLatitude = JavaMethod("()I")
    getLongitude = JavaMethod("()I")
    getNetworkId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")