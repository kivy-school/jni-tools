from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InetSocketAddress"]

class InetSocketAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/InetSocketAddress"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(I)V", False), ("(Ljava/net/InetAddress;I)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    getHostName = JavaMethod("()Ljava/lang/String;")
    isUnresolved = JavaMethod("()Z")
    getHostString = JavaMethod("()Ljava/lang/String;")
    createUnresolved = JavaStaticMethod("(Ljava/lang/String;I)Ljava/net/InetSocketAddress;")