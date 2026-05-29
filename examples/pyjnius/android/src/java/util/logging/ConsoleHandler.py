from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConsoleHandler"]

class ConsoleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/ConsoleHandler"
    __javaconstructor__ = [("()V", False)]
    close = JavaMethod("()V")
    publish = JavaMethod("(Ljava/util/logging/LogRecord;)V")