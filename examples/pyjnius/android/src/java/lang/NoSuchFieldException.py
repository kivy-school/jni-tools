from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchFieldException"]

class NoSuchFieldException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NoSuchFieldException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]