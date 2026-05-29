from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXRevocationChecker"]

class PKIXRevocationChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXRevocationChecker"
    getOptions = JavaMethod("()Ljava/util/Set;")
    clone = JavaMultipleMethod([("()Ljava/security/cert/PKIXRevocationChecker;", False, False), ("()Ljava/lang/Object;", False, False)])
    setOcspResponder = JavaMethod("(Ljava/net/URI;)V")
    getOcspResponder = JavaMethod("()Ljava/net/URI;")
    setOcspResponderCert = JavaMethod("(Ljava/security/cert/X509Certificate;)V")
    getOcspResponderCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    setOcspExtensions = JavaMethod("(Ljava/util/List;)V")
    getOcspExtensions = JavaMethod("()Ljava/util/List;")
    setOcspResponses = JavaMethod("(Ljava/util/Map;)V")
    getOcspResponses = JavaMethod("()Ljava/util/Map;")
    setOptions = JavaMethod("(Ljava/util/Set;)V")
    getSoftFailExceptions = JavaMethod("()Ljava/util/List;")

    class Option(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/PKIXRevocationChecker$Option"
        ONLY_END_ENTITY = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        PREFER_CRLS = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        NO_FALLBACK = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        SOFT_FAIL = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        values = JavaStaticMethod("()[Ljava/security/cert/PKIXRevocationChecker$Option;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/PKIXRevocationChecker$Option;")
        ONLY_END_ENTITY = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        PREFER_CRLS = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        NO_FALLBACK = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")
        SOFT_FAIL = JavaStaticField("Ljava/security/cert/PKIXRevocationChecker$Option;")