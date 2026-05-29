from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SigningInfo"]

class SigningInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/SigningInfo"
    __javaconstructor__ = [("(ILjava/util/Collection;Ljava/util/Collection;Ljava/util/Collection;)V", False), ("(Landroid/content/pm/SigningInfo;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    VERSION_JAR = JavaStaticField("I")
    VERSION_SIGNING_BLOCK_V2 = JavaStaticField("I")
    VERSION_SIGNING_BLOCK_V3 = JavaStaticField("I")
    VERSION_SIGNING_BLOCK_V4 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasMultipleSigners = JavaMethod("()Z")
    getSchemeVersion = JavaMethod("()I")
    getPublicKeys = JavaMethod("()Ljava/util/Collection;")
    getApkContentsSigners = JavaMethod("()[Landroid/content/pm/Signature;")
    getSigningCertificateHistory = JavaMethod("()[Landroid/content/pm/Signature;")
    hasPastSigningCertificates = JavaMethod("()Z")
    signersMatchExactly = JavaMethod("(Landroid/content/pm/SigningInfo;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")