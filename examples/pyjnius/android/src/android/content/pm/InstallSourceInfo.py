from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstallSourceInfo"]

class InstallSourceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/InstallSourceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPackageSource = JavaMethod("()I")
    getInitiatingPackageName = JavaMethod("()Ljava/lang/String;")
    getInitiatingPackageSigningInfo = JavaMethod("()Landroid/content/pm/SigningInfo;")
    getInstallingPackageName = JavaMethod("()Ljava/lang/String;")
    getOriginatingPackageName = JavaMethod("()Ljava/lang/String;")
    getUpdateOwnerPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")