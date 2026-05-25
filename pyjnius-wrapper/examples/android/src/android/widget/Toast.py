from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Toast"]

class Toast(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Toast"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    LENGTH_LONG = JavaStaticField("I")
    LENGTH_SHORT = JavaStaticField("I")
    show = JavaMethod("()V")
    cancel = JavaMethod("()V")
    setView = JavaMethod("(Landroid/view/View;)V")
    getView = JavaMethod("()Landroid/view/View;")
    setDuration = JavaMethod("(I)V")
    getDuration = JavaMethod("()I")
    setMargin = JavaMethod("(FF)V")
    getHorizontalMargin = JavaMethod("()F")
    getVerticalMargin = JavaMethod("()F")
    setGravity = JavaMethod("(III)V")
    getGravity = JavaMethod("()I")
    getXOffset = JavaMethod("()I")
    getYOffset = JavaMethod("()I")
    addCallback = JavaMethod("(Landroid/widget/Toast$Callback;)V")
    removeCallback = JavaMethod("(Landroid/widget/Toast$Callback;)V")
    makeText = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;", True, False), ("(Landroid/content/Context;II)Landroid/widget/Toast;", True, False)])
    setText = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Toast/Callback"
        __javaconstructor__ = [("()V", False)]
        onToastShown = JavaMethod("()V")
        onToastHidden = JavaMethod("()V")