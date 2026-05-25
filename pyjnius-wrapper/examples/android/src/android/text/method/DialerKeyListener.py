from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialerKeyListener"]

class DialerKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/DialerKeyListener"
    __javaconstructor__ = [("()V", False)]
    CHARACTERS = JavaStaticField("[C")
    getAcceptedChars = JavaMethod("()[C")
    getInstance = JavaStaticMethod("()Landroid/text/method/DialerKeyListener;")
    getInputType = JavaMethod("()I")
    lookup = JavaMethod("(Landroid/view/KeyEvent;Landroid/text/Spannable;)I")