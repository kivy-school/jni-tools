from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialDescription"]

class CredentialDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialDescription"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Set;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getType = JavaMethod("()Ljava/lang/String;")
    getSupportedElementKeys = JavaMethod("()Ljava/util/Set;")
    getCredentialEntries = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")