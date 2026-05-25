from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContextThemeWrapper"]

class ContextThemeWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ContextThemeWrapper"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/content/res/Resources$Theme;)V", False)]
    attachBaseContext = JavaMethod("(Landroid/content/Context;)V")
    applyOverrideConfiguration = JavaMethod("(Landroid/content/res/Configuration;)V")
    getAssets = JavaMethod("()Landroid/content/res/AssetManager;")
    getResources = JavaMethod("()Landroid/content/res/Resources;")
    setTheme = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/content/res/Resources$Theme;)V", False, False)])
    getTheme = JavaMethod("()Landroid/content/res/Resources$Theme;")
    getSystemService = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    onApplyThemeResource = JavaMethod("(Landroid/content/res/Resources$Theme;IZ)V")