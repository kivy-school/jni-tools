from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProgressDialog"]

class ProgressDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ProgressDialog"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False)]
    STYLE_HORIZONTAL = JavaStaticField("I")
    STYLE_SPINNER = JavaStaticField("I")
    THEME_DEVICE_DEFAULT_DARK = JavaStaticField("I")
    THEME_DEVICE_DEFAULT_LIGHT = JavaStaticField("I")
    THEME_HOLO_DARK = JavaStaticField("I")
    THEME_HOLO_LIGHT = JavaStaticField("I")
    THEME_TRADITIONAL = JavaStaticField("I")
    BUTTON1 = JavaStaticField("I")
    BUTTON2 = JavaStaticField("I")
    BUTTON3 = JavaStaticField("I")
    BUTTON_NEGATIVE = JavaStaticField("I")
    BUTTON_NEUTRAL = JavaStaticField("I")
    BUTTON_POSITIVE = JavaStaticField("I")
    setProgressStyle = JavaMethod("(I)V")
    setProgressNumberFormat = JavaMethod("(Ljava/lang/String;)V")
    setProgressPercentFormat = JavaMethod("(Ljava/text/NumberFormat;)V")
    setMessage = JavaMethod("(Ljava/lang/CharSequence;)V")
    show = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZLandroid/content/DialogInterface$OnCancelListener;)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;ZZ)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;Z)Landroid/app/ProgressDialog;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/app/ProgressDialog;", True, False)])
    getMax = JavaMethod("()I")
    getProgress = JavaMethod("()I")
    getSecondaryProgress = JavaMethod("()I")
    incrementProgressBy = JavaMethod("(I)V")
    incrementSecondaryProgressBy = JavaMethod("(I)V")
    isIndeterminate = JavaMethod("()Z")
    setIndeterminate = JavaMethod("(Z)V")
    setIndeterminateDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    onStart = JavaMethod("()V")
    setProgress = JavaMethod("(I)V")
    setProgressDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setSecondaryProgress = JavaMethod("(I)V")
    setMax = JavaMethod("(I)V")