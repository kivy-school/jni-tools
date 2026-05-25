from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterfaceAddress"]

class InterfaceAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/InterfaceAddress"
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getBroadcast = JavaMethod("()Ljava/net/InetAddress;")
    getNetworkPrefixLength = JavaMethod("()S")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")