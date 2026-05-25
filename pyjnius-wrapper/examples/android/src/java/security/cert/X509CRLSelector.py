from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRLSelector"]

class X509CRLSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRLSelector"
    __javaconstructor__ = [("()V", False)]
    setIssuers = JavaMethod("(Ljava/util/Collection;)V")
    setIssuerNames = JavaMethod("(Ljava/util/Collection;)V")
    addIssuer = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)V")
    addIssuerName = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("([B)V", False, False)])
    setMinCRLNumber = JavaMethod("(Ljava/math/BigInteger;)V")
    setMaxCRLNumber = JavaMethod("(Ljava/math/BigInteger;)V")
    setDateAndTime = JavaMethod("(Ljava/util/Date;)V")
    setCertificateChecking = JavaMethod("(Ljava/security/cert/X509Certificate;)V")
    getIssuers = JavaMethod("()Ljava/util/Collection;")
    getIssuerNames = JavaMethod("()Ljava/util/Collection;")
    getMinCRL = JavaMethod("()Ljava/math/BigInteger;")
    getMaxCRL = JavaMethod("()Ljava/math/BigInteger;")
    getDateAndTime = JavaMethod("()Ljava/util/Date;")
    getCertificateChecking = JavaMethod("()Ljava/security/cert/X509Certificate;")
    toString = JavaMethod("()Ljava/lang/String;")
    match = JavaMethod("(Ljava/security/cert/CRL;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")