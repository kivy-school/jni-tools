from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetCredentialRequest"]

class GetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCredentialOptions = JavaMethod("()Ljava/util/List;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/GetCredentialRequest/Builder"
        __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
        addCredentialOption = JavaMethod("(Landroid/credentials/CredentialOption;)Landroid/credentials/GetCredentialRequest$Builder;")
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/GetCredentialRequest$Builder;")
        setCredentialOptions = JavaMethod("(Ljava/util/List;)Landroid/credentials/GetCredentialRequest$Builder;")
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/GetCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/GetCredentialRequest;")