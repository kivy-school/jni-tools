from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class X509Extension(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Extension"
    hasUnsupportedCriticalExtension = JavaMethod("()Z")
    getCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")
    getNonCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")
    getExtensionValue = JavaMethod("(Ljava/lang/String;)[B")

class PolicyQualifierInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyQualifierInfo"
    __javaconstructor__ = [("([B)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifierId = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifier = JavaMethod("()[B")
    getEncoded = JavaMethod("()[B")

class X509CRLEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRLEntry"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")
    getCertificateIssuer = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    getEncoded = JavaMethod("()[B")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    hasExtensions = JavaMethod("()Z")

class CertificateFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False), ("(Ljava/lang/String;)Ljava/security/cert/CertificateFactory;", True, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    getCertPathEncodings = JavaMethod("()Ljava/util/Iterator;")
    generateCertificates = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    generateCRL = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/CRL;")
    generateCRLs = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    generateCertificate = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/Certificate;")
    generateCertPath = JavaMultipleMethod([("(Ljava/io/InputStream;Ljava/lang/String;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/util/List;)Ljava/security/cert/CertPath;", False, False)])

class CollectionCertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CollectionCertStoreParameters"
    __javaconstructor__ = [("(Ljava/util/Collection;)V", False), ("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getCollection = JavaMethod("()Ljava/util/Collection;")

class CertPathBuilderSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderSpi"
    __javaconstructor__ = [("()V", False)]
    engineBuild = JavaMethod("(Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathBuilderResult;")
    engineGetRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")

class LDAPCertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/LDAPCertStoreParameters"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getPort = JavaMethod("()I")
    getServerName = JavaMethod("()Ljava/lang/String;")

class X509CertSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CertSelector"
    __javaconstructor__ = [("()V", False)]
    getCertificate = JavaMethod("()Ljava/security/cert/X509Certificate;")
    setCertificate = JavaMethod("(Ljava/security/cert/X509Certificate;)V")
    setSerialNumber = JavaMethod("(Ljava/math/BigInteger;)V")
    setSubject = JavaMultipleMethod([("(Ljavax/security/auth/x500/X500Principal;)V", False, False), ("([B)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    getSubject = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/Certificate;)Z")
    setPathToNames = JavaMethod("(Ljava/util/Collection;)V")
    addPathToName = JavaMultipleMethod([("(I[B)V", False, False), ("(ILjava/lang/String;)V", False, False)])
    getIssuer = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getIssuerAsBytes = JavaMethod("()[B")
    getSubjectAsBytes = JavaMethod("()[B")
    getSubjectKeyIdentifier = JavaMethod("()[B")
    getAuthorityKeyIdentifier = JavaMethod("()[B")
    getCertificateValid = JavaMethod("()Ljava/util/Date;")
    getPrivateKeyValid = JavaMethod("()Ljava/util/Date;")
    getSubjectPublicKeyAlgID = JavaMethod("()Ljava/lang/String;")
    getSubjectPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    getMatchAllSubjectAltNames = JavaMethod("()Z")
    getNameConstraints = JavaMethod("()[B")
    getPolicy = JavaMethod("()Ljava/util/Set;")
    getPathToNames = JavaMethod("()Ljava/util/Collection;")
    getBasicConstraints = JavaMethod("()I")
    getExtendedKeyUsage = JavaMethod("()Ljava/util/Set;")
    getSubjectAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getKeyUsage = JavaMethod("()[Z")
    getIssuerAsString = JavaMethod("()Ljava/lang/String;")
    getSubjectAsString = JavaMethod("()Ljava/lang/String;")
    setIssuer = JavaMultipleMethod([("(Ljavax/security/auth/x500/X500Principal;)V", False, False), ("([B)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setSubjectKeyIdentifier = JavaMethod("([B)V")
    setAuthorityKeyIdentifier = JavaMethod("([B)V")
    setCertificateValid = JavaMethod("(Ljava/util/Date;)V")
    setPrivateKeyValid = JavaMethod("(Ljava/util/Date;)V")
    setSubjectPublicKeyAlgID = JavaMethod("(Ljava/lang/String;)V")
    setSubjectPublicKey = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("([B)V", False, False)])
    setKeyUsage = JavaMethod("([Z)V")
    setExtendedKeyUsage = JavaMethod("(Ljava/util/Set;)V")
    setMatchAllSubjectAltNames = JavaMethod("(Z)V")
    setSubjectAlternativeNames = JavaMethod("(Ljava/util/Collection;)V")
    addSubjectAlternativeName = JavaMultipleMethod([("(I[B)V", False, False), ("(ILjava/lang/String;)V", False, False)])
    setNameConstraints = JavaMethod("([B)V")
    setBasicConstraints = JavaMethod("(I)V")
    setPolicy = JavaMethod("(Ljava/util/Set;)V")

class CertSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertSelector"
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/Certificate;)Z")

class CertificateNotYetValidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateNotYetValidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Extension(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Extension"
    encode = JavaMethod("(Ljava/io/OutputStream;)V")
    getValue = JavaMethod("()[B")
    getId = JavaMethod("()Ljava/lang/String;")
    isCritical = JavaMethod("()Z")

class CertPathBuilderException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CRLException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CertPathValidatorResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorResult"
    clone = JavaMethod("()Ljava/lang/Object;")

class CertificateFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineGenerateCertificate = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/Certificate;")
    engineGetCertPathEncodings = JavaMethod("()Ljava/util/Iterator;")
    engineGenerateCertPath = JavaMultipleMethod([("(Ljava/util/List;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;Ljava/lang/String;)Ljava/security/cert/CertPath;", False, False), ("(Ljava/io/InputStream;)Ljava/security/cert/CertPath;", False, False)])
    engineGenerateCertificates = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")
    engineGenerateCRL = JavaMethod("(Ljava/io/InputStream;)Ljava/security/cert/CRL;")
    engineGenerateCRLs = JavaMethod("(Ljava/io/InputStream;)Ljava/util/Collection;")

class PKIXCertPathValidatorResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathValidatorResult"
    __javaconstructor__ = [("(Ljava/security/cert/TrustAnchor;Ljava/security/cert/PolicyNode;Ljava/security/PublicKey;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    getTrustAnchor = JavaMethod("()Ljava/security/cert/TrustAnchor;")
    getPolicyTree = JavaMethod("()Ljava/security/cert/PolicyNode;")

class CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRL"
    isRevoked = JavaMethod("(Ljava/security/cert/Certificate;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")

class CertStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStore"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/security/Provider;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;Ljava/lang/String;)Ljava/security/cert/CertStore;", True, False), ("(Ljava/lang/String;Ljava/security/cert/CertStoreParameters;)Ljava/security/cert/CertStore;", True, False)])
    getCertificates = JavaMethod("(Ljava/security/cert/CertSelector;)Ljava/util/Collection;")
    getType = JavaMethod("()Ljava/lang/String;")
    getCRLs = JavaMethod("(Ljava/security/cert/CRLSelector;)Ljava/util/Collection;")
    getCertStoreParameters = JavaMethod("()Ljava/security/cert/CertStoreParameters;")

class PKIXRevocationChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXRevocationChecker"
    clone = JavaMultipleMethod([("()Ljava/security/cert/PKIXRevocationChecker;", False, False), ("()Ljava/lang/Object;", False, False)])
    getOptions = JavaMethod("()Ljava/util/Set;")
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

class CertPathValidatorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;Ljava/security/cert/CertPath;ILjava/security/cert/CertPathValidatorException$Reason;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;Ljava/security/cert/CertPath;I)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    getIndex = JavaMethod("()I")
    getReason = JavaMethod("()Ljava/security/cert/CertPathValidatorException$Reason;")
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")

    class BasicReason(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/CertPathValidatorException$BasicReason"
        UNSPECIFIED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        EXPIRED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        NOT_YET_VALID = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        REVOKED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        UNDETERMINED_REVOCATION_STATUS = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        INVALID_SIGNATURE = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        ALGORITHM_CONSTRAINED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        values = JavaStaticMethod("()[Ljava/security/cert/CertPathValidatorException$BasicReason;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/CertPathValidatorException$BasicReason;")
        UNSPECIFIED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        EXPIRED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        NOT_YET_VALID = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        REVOKED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        UNDETERMINED_REVOCATION_STATUS = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        INVALID_SIGNATURE = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")
        ALGORITHM_CONSTRAINED = JavaStaticField("Ljava/security/cert/CertPathValidatorException$BasicReason;")

    class Reason(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/CertPathValidatorException$Reason"

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Certificate"
    getVersion = JavaMethod("()I")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSubjectX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSignature = JavaMethod("()[B")
    getBasicConstraints = JavaMethod("()I")
    getExtendedKeyUsage = JavaMethod("()Ljava/util/List;")
    getSubjectAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getIssuerAlternativeNames = JavaMethod("()Ljava/util/Collection;")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    getTBSCertificate = JavaMethod("()[B")
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getIssuerUniqueID = JavaMethod("()[Z")
    getSubjectUniqueID = JavaMethod("()[Z")
    getKeyUsage = JavaMethod("()[Z")
    verify = JavaMethod("(Ljava/security/PublicKey;Ljava/security/Provider;)V")

class PKIXCertPathChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathChecker"
    getSupportedExtensions = JavaMethod("()Ljava/util/Set;")
    clone = JavaMethod("()Ljava/lang/Object;")
    init = JavaMethod("(Z)V")
    check = JavaMultipleMethod([("(Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/security/cert/Certificate;Ljava/util/Collection;)V", False, False)])
    isForwardCheckingSupported = JavaMethod("()Z")

class CertificateEncodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateEncodingException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CertificateRevokedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateRevokedException"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CRLReason;Ljavax/security/auth/x500/X500Principal;Ljava/util/Map;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getRevocationReason = JavaMethod("()Ljava/security/cert/CRLReason;")
    getRevocationDate = JavaMethod("()Ljava/util/Date;")
    getAuthorityName = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getInvalidityDate = JavaMethod("()Ljava/util/Date;")
    getExtensions = JavaMethod("()Ljava/util/Map;")

class CertStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class PKIXReason(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXReason"
    NAME_CHAINING = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_KEY_USAGE = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_POLICY = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NO_TRUST_ANCHOR = JavaStaticField("Ljava/security/cert/PKIXReason;")
    UNRECOGNIZED_CRIT_EXT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NOT_CA_CERT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    PATH_TOO_LONG = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_NAME = JavaStaticField("Ljava/security/cert/PKIXReason;")
    values = JavaStaticMethod("()[Ljava/security/cert/PKIXReason;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/PKIXReason;")
    NAME_CHAINING = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_KEY_USAGE = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_POLICY = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NO_TRUST_ANCHOR = JavaStaticField("Ljava/security/cert/PKIXReason;")
    UNRECOGNIZED_CRIT_EXT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NOT_CA_CERT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    PATH_TOO_LONG = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_NAME = JavaStaticField("Ljava/security/cert/PKIXReason;")

class CertPathValidatorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorSpi"
    __javaconstructor__ = [("()V", False)]
    engineValidate = JavaMethod("(Ljava/security/cert/CertPath;Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathValidatorResult;")
    engineGetRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")

class TrustAnchor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/TrustAnchor"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/PublicKey;[B)V", False), ("(Ljavax/security/auth/x500/X500Principal;Ljava/security/PublicKey;[B)V", False), ("(Ljava/security/cert/X509Certificate;[B)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getNameConstraints = JavaMethod("()[B")
    getTrustedCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getCA = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getCAName = JavaMethod("()Ljava/lang/String;")
    getCAPublicKey = JavaMethod("()Ljava/security/PublicKey;")

class CertificateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CertificateExpiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateExpiredException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class CertStoreSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreSpi"
    __javaconstructor__ = [("(Ljava/security/cert/CertStoreParameters;)V", False)]
    engineGetCertificates = JavaMethod("(Ljava/security/cert/CertSelector;)Ljava/util/Collection;")
    engineGetCRLs = JavaMethod("(Ljava/security/cert/CRLSelector;)Ljava/util/Collection;")

class PKIXBuilderParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXBuilderParameters"
    __javaconstructor__ = [("(Ljava/util/Set;Ljava/security/cert/CertSelector;)V", False), ("(Ljava/security/KeyStore;Ljava/security/cert/CertSelector;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    setMaxPathLength = JavaMethod("(I)V")
    getMaxPathLength = JavaMethod("()I")

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Certificate"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False)])
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")

class CertPathBuilderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilderResult"
    clone = JavaMethod("()Ljava/lang/Object;")
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")

class CertificateParsingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateParsingException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CertPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPath"
    getEncodings = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCertificates = JavaMethod("()Ljava/util/List;")
    getType = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMultipleMethod([("()[B", False, False), ("(Ljava/lang/String;)[B", False, False)])

class CertPathBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathBuilder"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathBuilder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathBuilder;", True, False)])
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")
    build = JavaMethod("(Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathBuilderResult;")

class PKIXCertPathBuilderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXCertPathBuilderResult"
    __javaconstructor__ = [("(Ljava/security/cert/CertPath;Ljava/security/cert/TrustAnchor;Ljava/security/cert/PolicyNode;Ljava/security/PublicKey;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")

class PolicyNode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyNode"
    getChildren = JavaMethod("()Ljava/util/Iterator;")
    getParent = JavaMethod("()Ljava/security/cert/PolicyNode;")
    getDepth = JavaMethod("()I")
    isCritical = JavaMethod("()Z")
    getValidPolicy = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifiers = JavaMethod("()Ljava/util/Set;")
    getExpectedPolicies = JavaMethod("()Ljava/util/Set;")

class PKIXParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXParameters"
    __javaconstructor__ = [("(Ljava/util/Set;)V", False), ("(Ljava/security/KeyStore;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    setTargetCertConstraints = JavaMethod("(Ljava/security/cert/CertSelector;)V")
    setTrustAnchors = JavaMethod("(Ljava/util/Set;)V")
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
    getDate = JavaMethod("()Ljava/util/Date;")
    setDate = JavaMethod("(Ljava/util/Date;)V")

class CertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreParameters"
    clone = JavaMethod("()Ljava/lang/Object;")

class CRLSelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLSelector"
    clone = JavaMethod("()Ljava/lang/Object;")
    match = JavaMethod("(Ljava/security/cert/CRL;)Z")

class CertPathParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathParameters"
    clone = JavaMethod("()Ljava/lang/Object;")

class CertPathValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidator"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    validate = JavaMethod("(Ljava/security/cert/CertPath;Ljava/security/cert/CertPathParameters;)Ljava/security/cert/CertPathValidatorResult;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/cert/CertPathValidator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/cert/CertPathValidator;", True, False)])
    getRevocationChecker = JavaMethod("()Ljava/security/cert/CertPathChecker;")

class CRLReason(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLReason"
    UNSPECIFIED = JavaStaticField("Ljava/security/cert/CRLReason;")
    KEY_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    CA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    AFFILIATION_CHANGED = JavaStaticField("Ljava/security/cert/CRLReason;")
    SUPERSEDED = JavaStaticField("Ljava/security/cert/CRLReason;")
    CESSATION_OF_OPERATION = JavaStaticField("Ljava/security/cert/CRLReason;")
    CERTIFICATE_HOLD = JavaStaticField("Ljava/security/cert/CRLReason;")
    UNUSED = JavaStaticField("Ljava/security/cert/CRLReason;")
    REMOVE_FROM_CRL = JavaStaticField("Ljava/security/cert/CRLReason;")
    PRIVILEGE_WITHDRAWN = JavaStaticField("Ljava/security/cert/CRLReason;")
    AA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    values = JavaStaticMethod("()[Ljava/security/cert/CRLReason;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/CRLReason;")
    UNSPECIFIED = JavaStaticField("Ljava/security/cert/CRLReason;")
    KEY_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    CA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    AFFILIATION_CHANGED = JavaStaticField("Ljava/security/cert/CRLReason;")
    SUPERSEDED = JavaStaticField("Ljava/security/cert/CRLReason;")
    CESSATION_OF_OPERATION = JavaStaticField("Ljava/security/cert/CRLReason;")
    CERTIFICATE_HOLD = JavaStaticField("Ljava/security/cert/CRLReason;")
    UNUSED = JavaStaticField("Ljava/security/cert/CRLReason;")
    REMOVE_FROM_CRL = JavaStaticField("Ljava/security/cert/CRLReason;")
    PRIVILEGE_WITHDRAWN = JavaStaticField("Ljava/security/cert/CRLReason;")
    AA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")

class URICertStoreParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/URICertStoreParameters"
    __javaconstructor__ = [("(Ljava/net/URI;)V", False)]
    getURI = JavaMethod("()Ljava/net/URI;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/security/cert/URICertStoreParameters;", False, False), ("()Ljava/lang/Object;", False, False)])

class CertPathChecker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathChecker"
    init = JavaMethod("(Z)V")
    check = JavaMethod("(Ljava/security/cert/Certificate;)V")
    isForwardCheckingSupported = JavaMethod("()Z")

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

class X509CRL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509CRL"
    getVersion = JavaMethod("()I")
    getIssuerX500Principal = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getThisUpdate = JavaMethod("()Ljava/util/Date;")
    getNextUpdate = JavaMethod("()Ljava/util/Date;")
    getTBSCertList = JavaMethod("()[B")
    getRevokedCertificate = JavaMultipleMethod([("(Ljava/security/cert/X509Certificate;)Ljava/security/cert/X509CRLEntry;", False, False), ("(Ljava/math/BigInteger;)Ljava/security/cert/X509CRLEntry;", False, False)])
    getRevokedCertificates = JavaMethod("()Ljava/util/Set;")
    getSignature = JavaMethod("()[B")
    getEncoded = JavaMethod("()[B")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;)V", False, False)])