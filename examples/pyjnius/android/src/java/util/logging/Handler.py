from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Handler"]

class Handler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Handler"
    __javaconstructor__ = [("()V", False)]
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    setFormatter = JavaMethod("(Ljava/util/logging/Formatter;)V")
    getFormatter = JavaMethod("()Ljava/util/logging/Formatter;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setFilter = JavaMethod("(Ljava/util/logging/Filter;)V")
    getFilter = JavaMethod("()Ljava/util/logging/Filter;")
    setErrorManager = JavaMethod("(Ljava/util/logging/ErrorManager;)V")
    getErrorManager = JavaMethod("()Ljava/util/logging/ErrorManager;")
    reportError = JavaMethod("(Ljava/lang/String;Ljava/lang/Exception;I)V")
    setLevel = JavaMethod("(Ljava/util/logging/Level;)V")
    getLevel = JavaMethod("()Ljava/util/logging/Level;")
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")