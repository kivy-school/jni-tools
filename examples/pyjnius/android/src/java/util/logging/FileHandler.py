from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileHandler"]

class FileHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/FileHandler"
    __javaconstructor__ = [("(Ljava/lang/String;II)V", False), ("(Ljava/lang/String;IIZ)V", False), ("(Ljava/lang/String;)V", False), ("()V", False), ("(Ljava/lang/String;JIZ)V", False), ("(Ljava/lang/String;Z)V", False)]
    close = JavaMethod("()V")
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")