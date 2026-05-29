from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Formatter"]

class Formatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/Formatter"
    format = JavaMethod("(Ljava/util/logging/LogRecord;)Ljava/lang/String;")
    getHead = JavaMethod("(Ljava/util/logging/Handler;)Ljava/lang/String;")
    getTail = JavaMethod("(Ljava/util/logging/Handler;)Ljava/lang/String;")
    formatMessage = JavaMethod("(Ljava/util/logging/LogRecord;)Ljava/lang/String;")