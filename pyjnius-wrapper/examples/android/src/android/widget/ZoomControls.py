from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoomControls"]

class ZoomControls(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ZoomControls"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setOnZoomInClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    setOnZoomOutClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)V")
    setZoomSpeed = JavaMethod("(J)V")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    show = JavaMethod("()V")
    hide = JavaMethod("()V")
    setIsZoomInEnabled = JavaMethod("(Z)V")
    setIsZoomOutEnabled = JavaMethod("(Z)V")
    hasFocus = JavaMethod("()Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")