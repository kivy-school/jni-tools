from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchMethodException"]

class NoSuchMethodException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NoSuchMethodException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]