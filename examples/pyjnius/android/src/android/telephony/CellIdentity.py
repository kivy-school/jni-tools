from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellIdentity"]

class CellIdentity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellIdentity"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getOperatorAlphaLong = JavaMethod("()Ljava/lang/CharSequence;")
    getOperatorAlphaShort = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")