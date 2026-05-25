from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiTapKeyListener"]

class MultiTapKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/MultiTapKeyListener"
    __javaconstructor__ = [("(Landroid/text/method/TextKeyListener$Capitalize;Z)V", False)]
    getInstance = JavaStaticMethod("(ZLandroid/text/method/TextKeyListener$Capitalize;)Landroid/text/method/MultiTapKeyListener;")
    getInputType = JavaMethod("()I")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onSpanChanged = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;IIII)V")
    onSpanAdded = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanRemoved = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")