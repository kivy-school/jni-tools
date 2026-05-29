from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeRfc822AddrIdentification"]

class IkeRfc822AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeRfc822AddrIdentification"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    rfc822Name = JavaField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")