from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArchivedActivityInfo"]

class ArchivedActivityInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ArchivedActivityInfo"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/content/ComponentName;)V", False)]
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    setIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/content/pm/ArchivedActivityInfo;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getMonochromeIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setComponentName = JavaMethod("(Landroid/content/ComponentName;)Landroid/content/pm/ArchivedActivityInfo;")
    setLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/content/pm/ArchivedActivityInfo;")
    setMonochromeIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/content/pm/ArchivedActivityInfo;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")