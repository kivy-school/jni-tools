from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialOption"]

class CredentialOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialOption"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUPPORTED_ELEMENT_KEYS = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAllowedProviders = JavaMethod("()Ljava/util/Set;")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    getCredentialRetrievalData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CredentialOption$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CredentialOption$Builder;")
        addAllowedProvider = JavaMethod("(Landroid/content/ComponentName;)Landroid/credentials/CredentialOption$Builder;")
        setAllowedProviders = JavaMethod("(Ljava/util/Set;)Landroid/credentials/CredentialOption$Builder;")
        build = JavaMethod("()Landroid/credentials/CredentialOption;")