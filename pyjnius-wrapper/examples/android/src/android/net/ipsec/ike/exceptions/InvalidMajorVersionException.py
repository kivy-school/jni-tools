from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidMajorVersionException"]

class InvalidMajorVersionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidMajorVersionException"
    __javaconstructor__ = [("(B)V", False)]
    getMajorVersion = JavaMethod("()B")