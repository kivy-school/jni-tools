from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrowKeyMovementMethod"]

class ArrowKeyMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/ArrowKeyMovementMethod"
    __javaconstructor__ = [("()V", False)]
    nextParagraph = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    getInstance = JavaStaticMethod("()Landroid/text/method/MovementMethod;")
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    previousParagraph = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    canSelectArbitrarily = JavaMethod("()Z")