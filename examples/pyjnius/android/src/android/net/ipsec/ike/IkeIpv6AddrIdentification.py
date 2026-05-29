from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeIpv6AddrIdentification"]

class IkeIpv6AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeIpv6AddrIdentification"
    __javaconstructor__ = [("(Ljava/net/Inet6Address;)V", False)]
    ipv6Address = JavaField("Ljava/net/Inet6Address;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")