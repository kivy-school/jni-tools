from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetCredentialRequest"]

class GetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/GetCredentialRequest"
    __javaconstructor__ = [("(Landroid/service/credentials/CallingAppInfo;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    getCredentialOptions = JavaMethod("()Ljava/util/List;")