from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CancellationException"]

class CancellationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CancellationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]