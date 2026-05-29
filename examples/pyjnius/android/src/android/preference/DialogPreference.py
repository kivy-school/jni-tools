from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialogPreference"]

class DialogPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/DialogPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    getDialogIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getDialogLayoutResource = JavaMethod("()I")
    getDialogMessage = JavaMethod("()Ljava/lang/CharSequence;")
    getDialogTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getPositiveButtonText = JavaMethod("()Ljava/lang/CharSequence;")
    onActivityDestroy = JavaMethod("()V")
    setDialogIcon = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/graphics/drawable/Drawable;)V", False, False)])
    setDialogLayoutResource = JavaMethod("(I)V")
    setDialogMessage = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setDialogTitle = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    setNegativeButtonText = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setPositiveButtonText = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getDialog = JavaMethod("()Landroid/app/Dialog;")
    getNegativeButtonText = JavaMethod("()Ljava/lang/CharSequence;")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")