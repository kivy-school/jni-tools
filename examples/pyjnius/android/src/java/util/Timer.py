from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timer"]

class Timer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Timer"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Z)V", False), ("()V", False), ("(Ljava/lang/String;Z)V", False)]
    cancel = JavaMethod("()V")
    schedule = JavaMultipleMethod([("(Ljava/util/TimerTask;Ljava/util/Date;J)V", False, False), ("(Ljava/util/TimerTask;JJ)V", False, False), ("(Ljava/util/TimerTask;Ljava/util/Date;)V", False, False), ("(Ljava/util/TimerTask;J)V", False, False)])
    scheduleAtFixedRate = JavaMultipleMethod([("(Ljava/util/TimerTask;Ljava/util/Date;J)V", False, False), ("(Ljava/util/TimerTask;JJ)V", False, False)])
    purge = JavaMethod("()I")