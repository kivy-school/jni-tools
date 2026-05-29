from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdapterViewFlipper"]

class AdapterViewFlipper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/AdapterViewFlipper"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onAttachedToWindow = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    onWindowVisibilityChanged = JavaMethod("(I)V")
    setAdapter = JavaMethod("(Landroid/widget/Adapter;)V")
    getFlipInterval = JavaMethod("()I")
    setFlipInterval = JavaMethod("(I)V")
    startFlipping = JavaMethod("()V")
    stopFlipping = JavaMethod("()V")
    showNext = JavaMethod("()V")
    showPrevious = JavaMethod("()V")
    isFlipping = JavaMethod("()Z")
    setAutoStart = JavaMethod("(Z)V")
    isAutoStart = JavaMethod("()Z")
    fyiWillBeAdvancedByHostKThx = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")