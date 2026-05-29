from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvocationTargetException"]

class InvocationTargetException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/InvocationTargetException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    getTargetException = JavaMethod("()Ljava/lang/Throwable;")