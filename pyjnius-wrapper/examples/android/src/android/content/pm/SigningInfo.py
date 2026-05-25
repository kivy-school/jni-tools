from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SigningInfo"]

class SigningInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/SigningInfo"
    __javaconstructor__ = [("()V", False), ("(ILjava/util/Collection;Ljava/util/Collection;Ljava/util/Collection;)V", False), ("(Landroid/content/pm/SigningInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hasMultipleSigners = JavaMethod("()Z")
    hasPastSigningCertificates = JavaMethod("()Z")
    getSigningCertificateHistory = JavaMethod("()[Landroid/content/pm/Signature;")
    getApkContentsSigners = JavaMethod("()[Landroid/content/pm/Signature;")
    getSchemeVersion = JavaMethod("()I")
    getPublicKeys = JavaMethod("()Ljava/util/Collection;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")