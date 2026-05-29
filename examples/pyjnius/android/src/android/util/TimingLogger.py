from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimingLogger"]

class TimingLogger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/TimingLogger"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    dumpToLog = JavaMethod("()V")
    addSplit = JavaMethod("(Ljava/lang/String;)V")
    reset = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;Ljava/lang/String;)V", False, False)])