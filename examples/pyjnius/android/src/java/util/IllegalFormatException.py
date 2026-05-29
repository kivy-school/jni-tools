from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatException"]

class IllegalFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatException"