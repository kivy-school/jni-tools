from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MemoryHandler"]

class MemoryHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/MemoryHandler"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/logging/Handler;ILjava/util/logging/Level;)V", False)]
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    push = JavaMethod("()V")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    setPushLevel = JavaMethod("(Ljava/util/logging/Level;)V")
    getPushLevel = JavaMethod("()Ljava/util/logging/Level;")
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")