from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Handler"]

class Handler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Handler"
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    setFormatter = JavaMethod("(Ljava/util/logging/Formatter;)V")
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    getFormatter = JavaMethod("()Ljava/util/logging/Formatter;")
    setErrorManager = JavaMethod("(Ljava/util/logging/ErrorManager;)V")
    getErrorManager = JavaMethod("()Ljava/util/logging/ErrorManager;")
    setFilter = JavaMethod("(Ljava/util/logging/Filter;)V")
    getLevel = JavaMethod("()Ljava/util/logging/Level;")
    setLevel = JavaMethod("(Ljava/util/logging/Level;)V")
    getFilter = JavaMethod("()Ljava/util/logging/Filter;")