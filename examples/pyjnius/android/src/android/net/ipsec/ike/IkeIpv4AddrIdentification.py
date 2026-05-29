from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeIpv4AddrIdentification"]

class IkeIpv4AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeIpv4AddrIdentification"
    __javaconstructor__ = [("(Ljava/net/Inet4Address;)V", False)]
    ipv4Address = JavaField("Ljava/net/Inet4Address;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")