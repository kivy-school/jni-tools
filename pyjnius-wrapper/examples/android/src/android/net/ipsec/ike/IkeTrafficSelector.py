from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeTrafficSelector"]

class IkeTrafficSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeTrafficSelector"
    __javaconstructor__ = [("(IILjava/net/InetAddress;Ljava/net/InetAddress;)V", False)]
    endPort = JavaField("I")
    endingAddress = JavaField("Ljava/net/InetAddress;")
    startPort = JavaField("I")
    startingAddress = JavaField("Ljava/net/InetAddress;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")