from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProviderInfo"]

class ProviderInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ProviderInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/ProviderInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_SINGLE_USER = JavaStaticField("I")
    authority = JavaField("Ljava/lang/String;")
    flags = JavaField("I")
    forceUriPermissions = JavaField("Z")
    grantUriPermissions = JavaField("Z")
    initOrder = JavaField("I")
    isSyncable = JavaField("Z")
    multiprocess = JavaField("Z")
    pathPermissions = JavaField("[Landroid/content/pm/PathPermission;")
    readPermission = JavaField("Ljava/lang/String;")
    uriPermissionPatterns = JavaField("[Landroid/os/PatternMatcher;")
    writePermission = JavaField("Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")