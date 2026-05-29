from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkInterface"]

class NetworkInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/NetworkInterface"
    getInetAddresses = JavaMethod("()Ljava/util/Enumeration;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getParent = JavaMethod("()Ljava/net/NetworkInterface;")
    isVirtual = JavaMethod("()Z")
    getByName = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/NetworkInterface;")
    getInterfaceAddresses = JavaMethod("()Ljava/util/List;")
    getSubInterfaces = JavaMethod("()Ljava/util/Enumeration;")
    subInterfaces = JavaMethod("()Ljava/util/stream/Stream;")
    getByIndex = JavaStaticMethod("(I)Ljava/net/NetworkInterface;")
    getByInetAddress = JavaStaticMethod("(Ljava/net/InetAddress;)Ljava/net/NetworkInterface;")
    isUp = JavaMethod("()Z")
    isLoopback = JavaMethod("()Z")
    isPointToPoint = JavaMethod("()Z")
    supportsMulticast = JavaMethod("()Z")
    getHardwareAddress = JavaMethod("()[B")
    getMTU = JavaMethod("()I")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    inetAddresses = JavaMethod("()Ljava/util/stream/Stream;")
    getIndex = JavaMethod("()I")
    getNetworkInterfaces = JavaStaticMethod("()Ljava/util/Enumeration;")
    networkInterfaces = JavaStaticMethod("()Ljava/util/stream/Stream;")