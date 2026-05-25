from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BeginCreateCredentialRequest"]

class BeginCreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/BeginCreateCredentialRequest"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/service/credentials/CallingAppInfo;)V", False), ("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    getType = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Landroid/os/Bundle;")