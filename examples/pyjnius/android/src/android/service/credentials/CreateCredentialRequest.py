from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateCredentialRequest"]

class CreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/credentials/CreateCredentialRequest"
    __javaconstructor__ = [("(Landroid/service/credentials/CallingAppInfo;Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCallingAppInfo = JavaMethod("()Landroid/service/credentials/CallingAppInfo;")
    getType = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")