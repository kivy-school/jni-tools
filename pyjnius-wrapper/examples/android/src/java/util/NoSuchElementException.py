from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchElementException"]

class NoSuchElementException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/NoSuchElementException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False)]