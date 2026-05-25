from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeNonProtocolException"]

class IkeNonProtocolException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeNonProtocolException"