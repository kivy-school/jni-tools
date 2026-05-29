from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRLEntry"]

class X509CRLEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRLEntry"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    hasExtensions = JavaMethod("()Z")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")
    getCertificateIssuer = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")