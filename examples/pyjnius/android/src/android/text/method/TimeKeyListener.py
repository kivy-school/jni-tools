from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeKeyListener"]

class TimeKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/TimeKeyListener"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False)]
    CHARACTERS = JavaStaticField("[C")
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("()Landroid/text/method/TimeKeyListener;", True, False), ("(Ljava/util/Locale;)Landroid/text/method/TimeKeyListener;", True, False)])
    getInputType = JavaMethod("()I")