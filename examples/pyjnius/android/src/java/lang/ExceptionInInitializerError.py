from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExceptionInInitializerError"]

class ExceptionInInitializerError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ExceptionInInitializerError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False)]
    getException = JavaMethod("()Ljava/lang/Throwable;")