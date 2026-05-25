from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateCredentialRequest"]

class CreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CreateCredentialRequest"
    __javaconstructor__ = [("(Landroid/service/credentials/CallingAppInfo;Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    getType = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Landroid/os/Bundle;")