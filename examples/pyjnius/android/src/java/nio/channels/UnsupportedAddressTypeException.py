from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedAddressTypeException"]

class UnsupportedAddressTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/UnsupportedAddressTypeException"
    __javaconstructor__ = [("()V", False)]