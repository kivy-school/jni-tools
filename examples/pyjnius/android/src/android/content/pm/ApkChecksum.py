from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApkChecksum"]

class ApkChecksum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ApkChecksum"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getValue = JavaMethod("()[B")
    getType = JavaMethod("()I")
    getInstallerPackageName = JavaMethod("()Ljava/lang/String;")
    getSplitName = JavaMethod("()Ljava/lang/String;")
    getInstallerCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")