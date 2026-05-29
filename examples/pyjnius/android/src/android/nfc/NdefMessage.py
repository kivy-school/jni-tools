from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NdefMessage"]

class NdefMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NdefMessage"
    __javaconstructor__ = [("(Landroid/nfc/NdefRecord;[Landroid/nfc/NdefRecord;)V", True), ("([B)V", False), ("([Landroid/nfc/NdefRecord;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getByteArrayLength = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getRecords = JavaMethod("()[Landroid/nfc/NdefRecord;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")