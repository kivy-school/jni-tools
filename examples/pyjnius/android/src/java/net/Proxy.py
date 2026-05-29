from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Proxy"]

class Proxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Proxy"
    __javaconstructor__ = [("(Ljava/net/Proxy$Type;Ljava/net/SocketAddress;)V", False)]
    NO_PROXY = JavaStaticField("Ljava/net/Proxy;")
    type = JavaMethod("()Ljava/net/Proxy$Type;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    address = JavaMethod("()Ljava/net/SocketAddress;")

    class Type(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/net/Proxy$Type"
        DIRECT = JavaStaticField("Ljava/net/Proxy$Type;")
        HTTP = JavaStaticField("Ljava/net/Proxy$Type;")
        SOCKS = JavaStaticField("Ljava/net/Proxy$Type;")
        values = JavaStaticMethod("()[Ljava/net/Proxy$Type;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/Proxy$Type;")
        DIRECT = JavaStaticField("Ljava/net/Proxy$Type;")
        HTTP = JavaStaticField("Ljava/net/Proxy$Type;")
        SOCKS = JavaStaticField("Ljava/net/Proxy$Type;")