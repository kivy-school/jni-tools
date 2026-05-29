from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateCredentialRequest"]

class CreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    getCredentialData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CreateCredentialRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/CreateCredentialRequest$Builder;")
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/CreateCredentialRequest;")