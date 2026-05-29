from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringIndexOutOfBoundsException"]

class StringIndexOutOfBoundsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StringIndexOutOfBoundsException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(I)V", False)]