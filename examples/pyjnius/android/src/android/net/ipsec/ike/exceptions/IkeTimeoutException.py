from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeTimeoutException"]

class IkeTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeTimeoutException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]