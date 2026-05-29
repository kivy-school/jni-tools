from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NdefMessage"]

class NdefMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NdefMessage"
    __javaconstructor__ = [("([B)V", False), ("(Landroid/nfc/NdefRecord;[Landroid/nfc/NdefRecord;)V", True), ("([Landroid/nfc/NdefRecord;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getRecords = JavaMethod("()[Landroid/nfc/NdefRecord;")
    getByteArrayLength = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")