from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LauncherUserInfo"]

class LauncherUserInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/LauncherUserInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PRIVATE_SPACE_ENTRYPOINT_HIDDEN = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getUserType = JavaMethod("()Ljava/lang/String;")
    getUserConfig = JavaMethod("()Landroid/os/Bundle;")
    getUserSerialNumber = JavaMethod("()I")