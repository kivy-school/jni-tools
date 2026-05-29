from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnresolvedAddressException"]

class UnresolvedAddressException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/UnresolvedAddressException"
    __javaconstructor__ = [("()V", False)]