from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AvailableNfcAntenna"]

class AvailableNfcAntenna(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/AvailableNfcAntenna"
    __javaconstructor__ = [("(II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLocationX = JavaMethod("()I")
    getLocationY = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")