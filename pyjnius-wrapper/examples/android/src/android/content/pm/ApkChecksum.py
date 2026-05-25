from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApkChecksum"]

class ApkChecksum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ApkChecksum"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getType = JavaMethod("()I")
    getValue = JavaMethod("()[B")
    getInstallerCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
    getSplitName = JavaMethod("()Ljava/lang/String;")
    getInstallerPackageName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")