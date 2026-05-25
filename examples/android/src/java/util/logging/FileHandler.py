from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileHandler"]

class FileHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/FileHandler"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Z)V", False), ("(Ljava/lang/String;II)V", False), ("(Ljava/lang/String;IIZ)V", False)]
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    close = JavaMethod("()V")