from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberKeyListener"]

class NumberKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/NumberKeyListener"
    __javaconstructor__ = [("()V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")