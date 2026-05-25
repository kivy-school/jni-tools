from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZoomButton"]

class ZoomButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ZoomButton"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    setZoomSpeed = JavaMethod("(J)V")
    onLongClick = JavaMethod("(Landroid/view/View;)Z")
    onKeyUp = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    setEnabled = JavaMethod("(Z)V")
    dispatchUnhandledMove = JavaMethod("(Landroid/view/View;I)Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")