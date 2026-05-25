from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentity"]

class CellIdentity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentity"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    getOperatorAlphaLong = JavaMethod("()Ljava/lang/CharSequence;")
    getOperatorAlphaShort = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")