from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialogPreference"]

class DialogPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/DialogPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    setDialogTitle = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getDialogTitle = JavaMethod("()Ljava/lang/CharSequence;")
    setDialogMessage = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getDialogMessage = JavaMethod("()Ljava/lang/CharSequence;")
    setDialogIcon = JavaMultipleMethod([("(Landroid/graphics/drawable/Drawable;)V", False, False), ("(I)V", False, False)])
    getDialogIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setPositiveButtonText = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getPositiveButtonText = JavaMethod("()Ljava/lang/CharSequence;")
    setNegativeButtonText = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getNegativeButtonText = JavaMethod("()Ljava/lang/CharSequence;")
    setDialogLayoutResource = JavaMethod("(I)V")
    getDialogLayoutResource = JavaMethod("()I")
    onPrepareDialogBuilder = JavaMethod("(Landroid/app/AlertDialog$Builder;)V")
    onClick = JavaMultipleMethod([("()V", False, False), ("(Landroid/content/DialogInterface;I)V", False, False)])
    showDialog = JavaMethod("(Landroid/os/Bundle;)V")
    onCreateDialogView = JavaMethod("()Landroid/view/View;")
    onBindDialogView = JavaMethod("(Landroid/view/View;)V")
    onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")
    onDialogClosed = JavaMethod("(Z)V")
    getDialog = JavaMethod("()Landroid/app/Dialog;")
    onActivityDestroy = JavaMethod("()V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")