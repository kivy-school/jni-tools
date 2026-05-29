from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArchivedPackageInfo"]

class ArchivedPackageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ArchivedPackageInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/content/pm/SigningInfo;Ljava/util/List;)V", False)]
    getPackageName = JavaMethod("()Ljava/lang/String;")
    setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    getDefaultToDeviceProtectedStorage = JavaMethod("()Ljava/lang/String;")
    getLauncherActivities = JavaMethod("()Ljava/util/List;")
    getRequestLegacyExternalStorage = JavaMethod("()Ljava/lang/String;")
    getSigningInfo = JavaMethod("()Landroid/content/pm/SigningInfo;")
    getUserDataFragile = JavaMethod("()Ljava/lang/String;")
    getVersionCodeMajor = JavaMethod("()I")
    setDefaultToDeviceProtectedStorage = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setLauncherActivities = JavaMethod("(Ljava/util/List;)Landroid/content/pm/ArchivedPackageInfo;")
    setRequestLegacyExternalStorage = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setSigningInfo = JavaMethod("(Landroid/content/pm/SigningInfo;)Landroid/content/pm/ArchivedPackageInfo;")
    setTargetSdkVersion = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    setUserDataFragile = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/ArchivedPackageInfo;")
    setVersionCode = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    setVersionCodeMajor = JavaMethod("(I)Landroid/content/pm/ArchivedPackageInfo;")
    getTargetSdkVersion = JavaMethod("()I")
    getVersionCode = JavaMethod("()I")