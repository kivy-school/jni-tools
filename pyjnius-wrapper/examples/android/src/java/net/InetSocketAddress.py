from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InetSocketAddress"]

class InetSocketAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/InetSocketAddress"
    __javaconstructor__ = [("(I)V", False), ("(Ljava/net/InetAddress;I)V", False), ("(Ljava/lang/String;I)V", False)]
    createUnresolved = JavaStaticMethod("(Ljava/lang/String;I)Ljava/net/InetSocketAddress;")
    getPort = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getHostName = JavaMethod("()Ljava/lang/String;")
    getHostString = JavaMethod("()Ljava/lang/String;")
    isUnresolved = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")