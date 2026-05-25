from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketHandler"]

class SocketHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/SocketHandler"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;I)V", False)]
    close = JavaMethod("()V")
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")