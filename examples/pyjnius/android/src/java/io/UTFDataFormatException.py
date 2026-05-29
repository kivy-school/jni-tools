from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UTFDataFormatException"]

class UTFDataFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/UTFDataFormatException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]