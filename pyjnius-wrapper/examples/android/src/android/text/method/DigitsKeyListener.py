from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigitsKeyListener"]

class DigitsKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/DigitsKeyListener"
    __javaconstructor__ = [("()V", False), ("(ZZ)V", False), ("(Ljava/util/Locale;)V", False), ("(Ljava/util/Locale;ZZ)V", False)]
    getAcceptedChars = JavaMethod("()[C")
    getInstance = JavaMultipleMethod([("()Landroid/text/method/DigitsKeyListener;", True, False), ("(ZZ)Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/util/Locale;)Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/util/Locale;ZZ)Landroid/text/method/DigitsKeyListener;", True, False), ("(Ljava/lang/String;)Landroid/text/method/DigitsKeyListener;", True, False)])
    getInputType = JavaMethod("()I")
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")