from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialEntry"]

class CredentialEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CredentialEntry"
    __javaconstructor__ = [("(Landroid/service/credentials/BeginGetCredentialOption;Landroid/app/slice/Slice;)V", False), ("(Ljava/lang/String;Landroid/app/slice/Slice;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/app/slice/Slice;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBeginGetCredentialOptionId = JavaMethod("()Ljava/lang/String;")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    getType = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")