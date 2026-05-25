from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountDownTimer"]

class CountDownTimer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CountDownTimer"
    __javaconstructor__ = [("(JJ)V", False)]
    cancel = JavaMethod("()V")
    start = JavaMethod("()Landroid/os/CountDownTimer;")
    onTick = JavaMethod("(J)V")
    onFinish = JavaMethod("()V")