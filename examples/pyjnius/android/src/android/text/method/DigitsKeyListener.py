from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigitsKeyListener"]

class DigitsKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/DigitsKeyListener"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;ZZ)V", False), ("(Ljava/util/Locale;)V", False), ("(ZZ)V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
    getInstance = JavaMultipleMethod([("(ZZ)Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/lang/String;)Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/util/Locale;)Landroid/text/method/DigitsKeyListener;", True, False), ("()Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/util/Locale;ZZ)Landroid/text/method/DigitsKeyListener;", True, False)])
    getInputType = JavaMethod("()I")