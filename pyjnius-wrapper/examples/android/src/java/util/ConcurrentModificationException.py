from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentModificationException"]

class ConcurrentModificationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ConcurrentModificationException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]