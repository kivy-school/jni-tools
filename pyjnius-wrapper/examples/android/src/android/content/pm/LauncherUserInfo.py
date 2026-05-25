from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LauncherUserInfo"]

class LauncherUserInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/LauncherUserInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUserType = JavaMethod("()Ljava/lang/String;")
    getUserSerialNumber = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")