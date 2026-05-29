from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    banner = JavaField("I")
    icon = JavaField("I")
    isArchived = JavaField("Z")
    labelRes = JavaField("I")
    logo = JavaField("I")
    metaData = JavaField("Landroid/os/Bundle;")
    name = JavaField("Ljava/lang/String;")
    nonLocalizedLabel = JavaField("Ljava/lang/CharSequence;")
    packageName = JavaField("Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    loadDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")