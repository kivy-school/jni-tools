from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialOption"]

class CredentialOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialOption"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUPPORTED_ELEMENT_KEYS = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getCredentialRetrievalData = JavaMethod("()Landroid/os/Bundle;")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")
    getAllowedProviders = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CredentialOption/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CredentialOption$Builder;")
        addAllowedProvider = JavaMethod("(Landroid/content/ComponentName;)Landroid/credentials/CredentialOption$Builder;")
        setAllowedProviders = JavaMethod("(Ljava/util/Set;)Landroid/credentials/CredentialOption$Builder;")
        build = JavaMethod("()Landroid/credentials/CredentialOption;")