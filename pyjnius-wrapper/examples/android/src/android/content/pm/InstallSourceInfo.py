from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InstallSourceInfo"]

class InstallSourceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/InstallSourceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getInitiatingPackageName = JavaMethod("()Ljava/lang/String;")
    getInitiatingPackageSigningInfo = JavaMethod("()Landroid/content/pm/SigningInfo;")
    getOriginatingPackageName = JavaMethod("()Ljava/lang/String;")
    getInstallingPackageName = JavaMethod("()Ljava/lang/String;")
    getUpdateOwnerPackageName = JavaMethod("()Ljava/lang/String;")
    getPackageSource = JavaMethod("()I")