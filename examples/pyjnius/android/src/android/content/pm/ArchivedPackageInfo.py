from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArchivedPackageInfo"]

class ArchivedPackageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ArchivedPackageInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/content/pm/SigningInfo;Ljava/util/List;)V", False)]
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getSigningInfo = JavaMethod("()Landroid/content/pm/SigningInfo;")
    getVersionCode = JavaMethod("()I")
    getVersionCodeMajor = JavaMethod("()I")
    getTargetSdkVersion = JavaMethod("()I")
    getDefaultToDeviceProtectedStorage = JavaMethod("()Ljava/lang/String;")
    getRequestLegacyExternalStorage = JavaMethod("()Ljava/lang/String;")
    getUserDataFragile = JavaMethod("()Ljava/lang/String;")
    getLauncherActivities = JavaMethod("()Ljava/util/List;")
    setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setSigningInfo = JavaMethod("(Landroid/content/pm/SigningInfo;)Landroid/content/pm/ArchivedPackageInfo;")
    setVersionCode = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    setVersionCodeMajor = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    setTargetSdkVersion = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    setDefaultToDeviceProtectedStorage = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setRequestLegacyExternalStorage = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setUserDataFragile = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setLauncherActivities = JavaMethod("(Ljava/util/List;)Landroid/content/pm/ArchivedPackageInfo;")