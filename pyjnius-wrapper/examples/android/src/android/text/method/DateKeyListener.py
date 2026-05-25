from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DateKeyListener"]

class DateKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/DateKeyListener"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False)]
    CHARACTERS = JavaStaticField("[C")
    getInputType = JavaMethod("()I")
    getAcceptedChars = JavaMethod("()[C")
    getInstance = JavaMultipleMethod([("()Landroid/text/method/DateKeyListener;", True, False), ("(Ljava/util/Locale;)Landroid/text/method/DateKeyListener;", True, False)])