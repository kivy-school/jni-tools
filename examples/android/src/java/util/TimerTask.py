from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimerTask"]

class TimerTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TimerTask"
    __javaconstructor__ = [("()V", False)]
    run = JavaMethod("()V")
    cancel = JavaMethod("()Z")
    scheduledExecutionTime = JavaMethod("()J")