from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LauncherActivityInfo"]

class LauncherActivityInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/LauncherActivityInfo"
    getName = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getActivityInfo = JavaMethod("()Landroid/content/pm/ActivityInfo;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getBadgedIcon = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    getLoadingProgress = JavaMethod("()F")
    getFirstInstallTime = JavaMethod("()J")
    getApplicationInfo = JavaMethod("()Landroid/content/pm/ApplicationInfo;")
    getIcon = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")