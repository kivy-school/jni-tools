from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClearCredentialStateRequest"]

class ClearCredentialStateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/ClearCredentialStateRequest"
    __javaconstructor__ = [("(Landroid/service/credentials/CallingAppInfo;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")