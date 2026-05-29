from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetCredentialRequest"]

class GetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredentialOptions = JavaMethod("()Ljava/util/List;")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/GetCredentialRequest$Builder"
        __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/GetCredentialRequest$Builder;")
        addCredentialOption = JavaMethod("(Landroid/credentials/CredentialOption;)Landroid/credentials/GetCredentialRequest$Builder;")
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/GetCredentialRequest$Builder;")
        setCredentialOptions = JavaMethod("(Ljava/util/List;)Landroid/credentials/GetCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/GetCredentialRequest;")