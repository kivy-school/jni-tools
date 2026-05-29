from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssertionError"]

class AssertionError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/AssertionError"
    __javaconstructor__ = [("(I)V", False), ("(J)V", False), ("(F)V", False), ("(D)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("()V", False), ("(Ljava/lang/Object;)V", False), ("(Z)V", False), ("(C)V", False)]