from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataFormatException"]

class DataFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/DataFormatException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]