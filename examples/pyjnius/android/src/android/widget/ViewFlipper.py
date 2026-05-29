from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewFlipper"]

class ViewFlipper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ViewFlipper"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onWindowVisibilityChanged = JavaMethod("(I)V")
    setFlipInterval = JavaMethod("(I)V")
    getFlipInterval = JavaMethod("()I")
    startFlipping = JavaMethod("()V")
    stopFlipping = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    isFlipping = JavaMethod("()Z")
    setAutoStart = JavaMethod("(Z)V")
    isAutoStart = JavaMethod("()Z")