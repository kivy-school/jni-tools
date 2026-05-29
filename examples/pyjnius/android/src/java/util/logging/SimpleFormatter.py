from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimpleFormatter"]

class SimpleFormatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/SimpleFormatter"
    __javaconstructor__ = [("()V", False)]
    format = JavaMethod("(Ljava/util/logging/LogRecord;)Ljava/lang/String;")