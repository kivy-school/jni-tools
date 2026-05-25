from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EOFException"]

class EOFException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/EOFException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]