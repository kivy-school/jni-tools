from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PermissionGroupInfo"]

class PermissionGroupInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/PermissionGroupInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/PermissionGroupInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_PERSONAL_INFO = JavaStaticField("I")
    descriptionRes = JavaField("I")
    flags = JavaField("I")
    nonLocalizedDescription = JavaField("Ljava/lang/CharSequence;")
    priority = JavaField("I")
    loadDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")