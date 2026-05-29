from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509CRLSelector"]

class X509CRLSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRLSelector"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/CRL;)Z")
    setDateAndTime = JavaMethod("(Ljava/util/Date;)V")
    setIssuers = JavaMethod("(Ljava/util/Collection;)V")
    setIssuerNames = JavaMethod("(Ljava/util/Collection;)V")
    addIssuer = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)V")
    addIssuerName = JavaMultipleMethod([("([B)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setMinCRLNumber = JavaMethod("(Ljava/math/BigInteger;)V")
    setMaxCRLNumber = JavaMethod("(Ljava/math/BigInteger;)V")
    setCertificateChecking = JavaMethod("(Ljava/security/cert/X509Certificate;)V")
    getIssuers = JavaMethod("()Ljava/util/Collection;")
    getIssuerNames = JavaMethod("()Ljava/util/Collection;")
    getMinCRL = JavaMethod("()Ljava/math/BigInteger;")
    getMaxCRL = JavaMethod("()Ljava/math/BigInteger;")
    getDateAndTime = JavaMethod("()Ljava/util/Date;")
    getCertificateChecking = JavaMethod("()Ljava/security/cert/X509Certificate;")