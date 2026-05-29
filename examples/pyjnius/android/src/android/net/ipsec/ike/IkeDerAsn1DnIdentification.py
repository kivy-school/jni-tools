from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeDerAsn1DnIdentification"]

class IkeDerAsn1DnIdentification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeDerAsn1DnIdentification"
    __javaconstructor__ = [("(Ljavax/security/auth/x500/X500Principal;)V", False)]
    derAsn1Dn = JavaField("Ljavax/security/auth/x500/X500Principal;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")