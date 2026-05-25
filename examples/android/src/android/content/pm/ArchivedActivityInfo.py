from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArchivedActivityInfo"]

class ArchivedActivityInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ArchivedActivityInfo"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/content/ComponentName;)V", False)]
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getMonochromeIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/content/pm/ArchivedActivityInfo;")
    setComponentName = JavaMethod("(Landroid/content/ComponentName;)Landroid/content/pm/ArchivedActivityInfo;")
    setIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/content/pm/ArchivedActivityInfo;")
    setMonochromeIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/content/pm/ArchivedActivityInfo;")