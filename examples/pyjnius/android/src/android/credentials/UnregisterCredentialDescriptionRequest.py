from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnregisterCredentialDescriptionRequest"]

class UnregisterCredentialDescriptionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/UnregisterCredentialDescriptionRequest"
    __javaconstructor__ = [("(Landroid/credentials/CredentialDescription;)V", False), ("(Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredentialDescriptions = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")