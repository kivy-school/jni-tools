from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassNotFoundException"]

class ClassNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]
    getException = JavaMethod("()Ljava/lang/Throwable;")