from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Toast"]

class Toast(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Toast"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    LENGTH_LONG = JavaStaticField("I")
    LENGTH_SHORT = JavaStaticField("I")
    cancel = JavaMethod("()V")
    show = JavaMethod("()V")
    getGravity = JavaMethod("()I")
    setGravity = JavaMethod("(III)V")
    getDuration = JavaMethod("()I")
    setDuration = JavaMethod("(I)V")
    getView = JavaMethod("()Landroid/view/View;")
    setText = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    getXOffset = JavaMethod("()I")
    getYOffset = JavaMethod("()I")
    makeText = JavaMultipleMethod([("(Landroid/content/Context;II)Landroid/widget/Toast;", True, False), ("(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;", True, False)])
    getVerticalMargin = JavaMethod("()F")
    getHorizontalMargin = JavaMethod("()F")
    removeCallback = JavaMethod("(Landroid/widget/Toast$Callback;)V")
    setMargin = JavaMethod("(FF)V")
    setView = JavaMethod("(Landroid/view/View;)V")
    addCallback = JavaMethod("(Landroid/widget/Toast$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Toast$Callback"
        __javaconstructor__ = [("()V", False)]
        onToastHidden = JavaMethod("()V")
        onToastShown = JavaMethod("()V")