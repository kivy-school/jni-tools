from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkMovementMethod"]

class LinkMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/LinkMovementMethod"
    __javaconstructor__ = [("()V", False)]
    canSelectArbitrarily = JavaMethod("()Z")
    handleMovementKey = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;IILandroid/view/KeyEvent;)Z")
    up = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    down = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    left = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    right = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    getInstance = JavaStaticMethod("()Landroid/text/method/MovementMethod;")