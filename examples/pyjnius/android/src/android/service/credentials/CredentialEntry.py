from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialEntry"]

class CredentialEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CredentialEntry"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Landroid/app/slice/Slice;)V", False), ("(Landroid/service/credentials/BeginGetCredentialOption;Landroid/app/slice/Slice;)V", False), ("(Ljava/lang/String;Landroid/app/slice/Slice;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getBeginGetCredentialOptionId = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")