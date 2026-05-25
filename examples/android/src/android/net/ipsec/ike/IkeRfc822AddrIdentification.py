from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeRfc822AddrIdentification"]

class IkeRfc822AddrIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeRfc822AddrIdentification"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    rfc822Name = JavaField("Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")