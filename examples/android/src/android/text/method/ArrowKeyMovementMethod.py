from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrowKeyMovementMethod"]

class ArrowKeyMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/ArrowKeyMovementMethod"
    __javaconstructor__ = [("()V", False)]
    handleMovementKey = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;IILandroid/view/KeyEvent;)Z")
    left = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    right = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    up = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    down = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    pageUp = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    pageDown = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    top = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    bottom = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    lineStart = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    lineEnd = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    home = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    end = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    previousParagraph = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    nextParagraph = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)Z")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    canSelectArbitrarily = JavaMethod("()Z")
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    getInstance = JavaStaticMethod("()Landroid/text/method/MovementMethod;")