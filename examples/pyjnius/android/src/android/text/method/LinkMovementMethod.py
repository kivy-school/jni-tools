from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkMovementMethod"]

class LinkMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/LinkMovementMethod"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("()Landroid/text/method/MovementMethod;")
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    canSelectArbitrarily = JavaMethod("()Z")