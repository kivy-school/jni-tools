from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConsoleHandler"]

class ConsoleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/ConsoleHandler"
    __javaconstructor__ = [("()V", False)]
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")
    close = JavaMethod("()V")