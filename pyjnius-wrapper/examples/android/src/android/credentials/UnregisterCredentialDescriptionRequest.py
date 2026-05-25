from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnregisterCredentialDescriptionRequest"]

class UnregisterCredentialDescriptionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/UnregisterCredentialDescriptionRequest"
    __javaconstructor__ = [("(Landroid/credentials/CredentialDescription;)V", False), ("(Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCredentialDescriptions = JavaMethod("()Ljava/util/Set;")