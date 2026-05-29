from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimerTask"]

class TimerTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TimerTask"
    run = JavaMethod("()V")
    cancel = JavaMethod("()Z")
    scheduledExecutionTime = JavaMethod("()J")