from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetCredentialResponse"]

class GetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialResponse"
    __javaconstructor__ = [("(Landroid/credentials/Credential;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCredential = JavaMethod("()Landroid/credentials/Credential;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")