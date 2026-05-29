from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloneNotSupportedException"]

class CloneNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/CloneNotSupportedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]