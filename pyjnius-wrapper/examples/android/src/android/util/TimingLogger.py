from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimingLogger"]

class TimingLogger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/TimingLogger"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    reset = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("()V", False, False)])
    addSplit = JavaMethod("(Ljava/lang/String;)V")
    dumpToLog = JavaMethod("()V")