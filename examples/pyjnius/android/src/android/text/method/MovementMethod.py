from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MovementMethod"]

class MovementMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/MovementMethod"
    initialize = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)V")
    onGenericMotionEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onKeyDown = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onTrackballEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;ILandroid/view/KeyEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    onTakeFocus = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;I)V")
    canSelectArbitrarily = JavaMethod("()Z")
    onKeyOther = JavaMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/KeyEvent;)Z")