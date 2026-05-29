from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseMovementMethod"]

class BaseMovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/BaseMovementMethod"
    __javaconstructor__ = [("()V", False)]
    canSelectArbitrarily = JavaMethod("()Z")
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onKeyDown = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTrackballEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onGenericMotionEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    getMovementMetaState = JavaMethod("(Landroid/text/Spannable;Landroid/view/KeyEvent;)I")
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