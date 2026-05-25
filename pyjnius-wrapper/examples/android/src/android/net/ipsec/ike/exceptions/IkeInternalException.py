from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeInternalException"]

class IkeInternalException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeInternalException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]