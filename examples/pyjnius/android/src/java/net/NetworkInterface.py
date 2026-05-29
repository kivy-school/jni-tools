from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkInterface"]

class NetworkInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/NetworkInterface"
    getName = JavaMethod("()Ljava/lang/String;")
    getInetAddresses = JavaMethod("()Ljava/util/Enumeration;")
    getInterfaceAddresses = JavaMethod("()Ljava/util/List;")
    getSubInterfaces = JavaMethod("()Ljava/util/Enumeration;")
    getParent = JavaMethod("()Ljava/net/NetworkInterface;")
    getIndex = JavaMethod("()I")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    getByName = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/NetworkInterface;")
    getByIndex = JavaStaticMethod("(I)Ljava/net/NetworkInterface;")
    getByInetAddress = JavaStaticMethod("(Ljava/net/InetAddress;)Ljava/net/NetworkInterface;")
    getNetworkInterfaces = JavaStaticMethod("()Ljava/util/Enumeration;")
    isUp = JavaMethod("()Z")
    isLoopback = JavaMethod("()Z")
    isPointToPoint = JavaMethod("()Z")
    supportsMulticast = JavaMethod("()Z")
    getHardwareAddress = JavaMethod("()[B")
    getMTU = JavaMethod("()I")
    isVirtual = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")