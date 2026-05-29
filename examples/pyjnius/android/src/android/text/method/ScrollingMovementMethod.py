from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollingMovementMethod"]

class ScrollingMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/ScrollingMovementMethod"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("()Landroid/text/method/MovementMethod;")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")