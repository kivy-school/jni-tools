from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassNotFoundException"]

class ClassNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassNotFoundException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getException = JavaMethod("()Ljava/lang/Throwable;")