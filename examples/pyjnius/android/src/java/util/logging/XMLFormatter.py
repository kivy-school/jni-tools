from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLFormatter"]

class XMLFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/XMLFormatter"
    __javaconstructor__ = [("()V", False)]
    format = JavaMethod("(Ljava/util/logging/LogRecord;)Ljava/lang/String;")
    getHead = JavaMethod("(Ljava/util/logging/Handler;)Ljava/lang/String;")
    getTail = JavaMethod("(Ljava/util/logging/Handler;)Ljava/lang/String;")