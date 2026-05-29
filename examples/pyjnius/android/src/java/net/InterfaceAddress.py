from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterfaceAddress"]

class InterfaceAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/InterfaceAddress"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getNetworkPrefixLength = JavaMethod("()S")
    getBroadcast = JavaMethod("()Ljava/net/InetAddress;")