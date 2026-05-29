from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidObjectException"]

class InvalidObjectException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/InvalidObjectException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]