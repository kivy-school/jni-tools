from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExceptionInInitializerError"]

class ExceptionInInitializerError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ExceptionInInitializerError"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("()V", False)]
    getException = JavaMethod("()Ljava/lang/Throwable;")