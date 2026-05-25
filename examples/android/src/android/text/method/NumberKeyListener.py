from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberKeyListener"]

class NumberKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/NumberKeyListener"
    __javaconstructor__ = [("()V", False)]
    getAcceptedChars = JavaMethod("()[C")
    lookup = JavaMethod("(Landroid/view/KeyEvent;Landroid/text/Spannable;)I")
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
    ok = JavaStaticMethod("([CC)Z")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")