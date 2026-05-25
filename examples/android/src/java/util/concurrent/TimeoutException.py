from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeoutException"]

class TimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/TimeoutException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]