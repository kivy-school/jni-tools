from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseKeyListener"]

class BaseKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/BaseKeyListener"
    __javaconstructor__ = [("()V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    backspace = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    forwardDelete = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")