from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalDataException"]

class OptionalDataException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/OptionalDataException"
    length = JavaField("I")
    eof = JavaField("Z")