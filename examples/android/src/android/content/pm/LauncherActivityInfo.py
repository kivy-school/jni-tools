from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LauncherActivityInfo"]

class LauncherActivityInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/LauncherActivityInfo"
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getLoadingProgress = JavaMethod("()F")
    getIcon = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    getActivityInfo = JavaMethod("()Landroid/content/pm/ActivityInfo;")
    getApplicationInfo = JavaMethod("()Landroid/content/pm/ApplicationInfo;")
    getFirstInstallTime = JavaMethod("()J")
    getName = JavaMethod("()Ljava/lang/String;")
    getBadgedIcon = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")