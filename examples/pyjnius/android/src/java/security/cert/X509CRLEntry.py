from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRLEntry"]

class X509CRLEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRLEntry"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getCertificateIssuer = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    hasExtensions = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")