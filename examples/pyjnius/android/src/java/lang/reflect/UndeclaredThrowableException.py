from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UndeclaredThrowableException"]

class UndeclaredThrowableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/UndeclaredThrowableException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;Ljava/lang/String;)V", False)]
    getUndeclaredThrowable = JavaMethod("()Ljava/lang/Throwable;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")