from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeNetworkLostException"]

class IkeNetworkLostException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeNetworkLostException"
    __javaconstructor__ = [("(Landroid/net/Network;)V", False)]
    getNetwork = JavaMethod("()Landroid/net/Network;")