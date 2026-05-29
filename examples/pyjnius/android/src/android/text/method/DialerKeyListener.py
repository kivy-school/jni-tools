from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialerKeyListener"]

class DialerKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/DialerKeyListener"
    __javaconstructor__ = [("()V", False)]
    CHARACTERS = JavaStaticField("[C")
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    getInstance = JavaStaticMethod("()Landroid/text/method/DialerKeyListener;")
    getInputType = JavaMethod("()I")