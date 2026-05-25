from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamHandler"]

class StreamHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/StreamHandler"
    __javaconstructor__ = [("()V", False), ("(Ljava/io/OutputStream;Ljava/util/logging/Formatter;)V", False)]
    setOutputStream = JavaMethod("(Ljava/io/OutputStream;)V")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    isLoggable = JavaMethod("(Ljava/util/logging/LogRecord;)Z")
    flush = JavaMethod("()V")
    close = JavaMethod("()V")