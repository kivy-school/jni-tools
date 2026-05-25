from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateCredentialRequest"]

class CreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getType = JavaMethod("()Ljava/lang/String;")
    getCredentialData = JavaMethod("()Landroid/os/Bundle;")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CreateCredentialRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/CreateCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/CreateCredentialRequest;")