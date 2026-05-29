from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassCastException"]

class ClassCastException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassCastException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]