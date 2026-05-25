from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvocationTargetException"]

class InvocationTargetException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/InvocationTargetException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;Ljava/lang/String;)V", False)]
    getTargetException = JavaMethod("()Ljava/lang/Throwable;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")