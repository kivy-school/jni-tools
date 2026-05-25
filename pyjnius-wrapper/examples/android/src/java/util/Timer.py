from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timer"]

class Timer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Timer"
    __javaconstructor__ = [("()V", False), ("(Z)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Z)V", False)]
    schedule = JavaMultipleMethod([("(Ljava/util/TimerTask;J)V", False, False), ("(Ljava/util/TimerTask;Ljava/util/Date;)V", False, False), ("(Ljava/util/TimerTask;JJ)V", False, False), ("(Ljava/util/TimerTask;Ljava/util/Date;J)V", False, False)])
    scheduleAtFixedRate = JavaMultipleMethod([("(Ljava/util/TimerTask;JJ)V", False, False), ("(Ljava/util/TimerTask;Ljava/util/Date;J)V", False, False)])
    cancel = JavaMethod("()V")
    purge = JavaMethod("()I")