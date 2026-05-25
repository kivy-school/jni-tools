from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackView"]

class StackView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/StackView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    showNext = JavaMethod("()V")
    showPrevious = JavaMethod("()V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onGenericMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onInterceptTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onLayout = JavaMethod("(ZIIII)V")
    advance = JavaMethod("()V")
    onMeasure = JavaMethod("(II)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")