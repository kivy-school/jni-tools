from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MovementMethod"]

class MovementMethod(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/MovementMethod"
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onKeyDown = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/KeyEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    onTrackballEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onGenericMotionEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    canSelectArbitrarily = JavaMethod("()Z")