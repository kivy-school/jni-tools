from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXParameters"]

class PKIXParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXParameters"
    __javaconstructor__ = [("(Ljava/util/Set;)V", False), ("(Ljava/security/KeyStore;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    setTargetCertConstraints = JavaMethod("(Ljava/security/cert/CertSelector;)V")
    setTrustAnchors = JavaMethod("(Ljava/util/Set;)V")
    getDate = JavaMethod("()Ljava/util/Date;")
    setDate = JavaMethod("(Ljava/util/Date;)V")
    getTrustAnchors = JavaMethod("()Ljava/util/Set;")
    getInitialPolicies = JavaMethod("()Ljava/util/Set;")
    setInitialPolicies = JavaMethod("(Ljava/util/Set;)V")
    setCertStores = JavaMethod("(Ljava/util/List;)V")
    addCertStore = JavaMethod("(Ljava/security/cert/CertStore;)V")
    getCertStores = JavaMethod("()Ljava/util/List;")
    setRevocationEnabled = JavaMethod("(Z)V")
    isRevocationEnabled = JavaMethod("()Z")
    setExplicitPolicyRequired = JavaMethod("(Z)V")
    isExplicitPolicyRequired = JavaMethod("()Z")
    setPolicyMappingInhibited = JavaMethod("(Z)V")
    isPolicyMappingInhibited = JavaMethod("()Z")
    setAnyPolicyInhibited = JavaMethod("(Z)V")
    isAnyPolicyInhibited = JavaMethod("()Z")
    setPolicyQualifiersRejected = JavaMethod("(Z)V")
    getPolicyQualifiersRejected = JavaMethod("()Z")
    setCertPathCheckers = JavaMethod("(Ljava/util/List;)V")
    getCertPathCheckers = JavaMethod("()Ljava/util/List;")
    addCertPathChecker = JavaMethod("(Ljava/security/cert/PKIXCertPathChecker;)V")
    getSigProvider = JavaMethod("()Ljava/lang/String;")
    setSigProvider = JavaMethod("(Ljava/lang/String;)V")
    getTargetCertConstraints = JavaMethod("()Ljava/security/cert/CertSelector;")