from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProgressDialog"]

class ProgressDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ProgressDialog"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False)]
    STYLE_HORIZONTAL = JavaStaticField("I")
    STYLE_SPINNER = JavaStaticField("I")
    show = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;Z)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZ)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZLandroid/content/DialogInterface$OnCancelListener;)Landroid/app/ProgressDialog;", True, False)])
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onStart = JavaMethod("()V")
    onStop = JavaMethod("()V")
    setProgress = JavaMethod("(I)V")
    setSecondaryProgress = JavaMethod("(I)V")
    getProgress = JavaMethod("()I")
    getSecondaryProgress = JavaMethod("()I")
    getMax = JavaMethod("()I")
    setMax = JavaMethod("(I)V")
    incrementProgressBy = JavaMethod("(I)V")
    incrementSecondaryProgressBy = JavaMethod("(I)V")
    setProgressDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setIndeterminateDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setIndeterminate = JavaMethod("(Z)V")
    isIndeterminate = JavaMethod("()Z")
    setMessage = JavaMethod("(Ljava/lang/CharSequence;)V")
    setProgressStyle = JavaMethod("(I)V")
    setProgressNumberFormat = JavaMethod("(Ljava/lang/String;)V")
    setProgressPercentFormat = JavaMethod("(Ljava/text/NumberFormat;)V")