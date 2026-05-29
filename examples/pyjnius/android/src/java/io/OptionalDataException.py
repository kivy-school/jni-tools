from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalDataException"]

class OptionalDataException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/OptionalDataException"
    eof = JavaField("Z")
    length = JavaField("I")