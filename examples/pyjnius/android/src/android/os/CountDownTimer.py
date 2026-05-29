from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountDownTimer"]

class CountDownTimer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CountDownTimer"
    __javaconstructor__ = [("(JJ)V", False)]
    onTick = JavaMethod("(J)V")
    start = JavaMethod("()Landroid/os/CountDownTimer;")
    cancel = JavaMethod("()V")
    onFinish = JavaMethod("()V")