from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class KeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyFactory;", True, False), ("(Ljava/lang/String;)Ljava/security/KeyFactory;", True, False)])
    generatePublic = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PublicKey;")
    generatePrivate = JavaMethod("(Ljava/security/spec/KeySpec;)Ljava/security/PrivateKey;")
    getKeySpec = JavaMethod("(Ljava/security/Key;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljava/security/Key;)Ljava/security/Key;")

class PKCS12Attribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PKCS12Attribute"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("([B)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class SignatureSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignatureSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")

class Provider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Provider"
    configure = JavaMethod("(Ljava/lang/String;)Ljava/security/Provider;")
    getInfo = JavaMethod("()Ljava/lang/String;")
    getServices = JavaMethod("()Ljava/util/Set;")
    getVersion = JavaMethod("()D")
    getName = JavaMethod("()Ljava/lang/String;")
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False)])
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()Ljava/util/Collection;")
    load = JavaMethod("(Ljava/io/InputStream;)V")
    clear = JavaMethod("()V")
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False)])
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    keySet = JavaMethod("()Ljava/util/Set;")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    getService = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Provider$Service;")
    isConfigured = JavaMethod("()Z")
    getVersionStr = JavaMethod("()Ljava/lang/String;")

    class Service(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Provider$Service"
        __javaconstructor__ = [("(Ljava/security/Provider;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/List;Ljava/util/Map;)V", False)]
        getProvider = JavaMethod("()Ljava/security/Provider;")
        supportsParameter = JavaMethod("(Ljava/lang/Object;)Z")
        getAlgorithm = JavaMethod("()Ljava/lang/String;")
        getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")
        newInstance = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        getType = JavaMethod("()Ljava/lang/String;")
        getClassName = JavaMethod("()Ljava/lang/String;")

class AccessControlContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessControlContext"
    __javaconstructor__ = [("(Ljava/security/AccessControlContext;Ljava/security/DomainCombiner;)V", False), ("([Ljava/security/ProtectionDomain;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    checkPermission = JavaMethod("(Ljava/security/Permission;)V")
    getDomainCombiner = JavaMethod("()Ljava/security/DomainCombiner;")

class DrbgParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DrbgParameters"
    nextBytes = JavaStaticMethod("(IZ[B)Ljava/security/DrbgParameters$NextBytes;")
    reseed = JavaStaticMethod("(Z[B)Ljava/security/DrbgParameters$Reseed;")
    instantiation = JavaStaticMethod("(ILjava/security/DrbgParameters$Capability;[B)Ljava/security/DrbgParameters$Instantiation;")

    class Instantiation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Instantiation"
        getStrength = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        getCapability = JavaMethod("()Ljava/security/DrbgParameters$Capability;")
        getPersonalizationString = JavaMethod("()[B")

    class Capability(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Capability"
        PR_AND_RESEED = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        RESEED_ONLY = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        NONE = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        toString = JavaMethod("()Ljava/lang/String;")
        values = JavaStaticMethod("()[Ljava/security/DrbgParameters$Capability;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/DrbgParameters$Capability;")
        supportsReseeding = JavaMethod("()Z")
        supportsPredictionResistance = JavaMethod("()Z")
        PR_AND_RESEED = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        RESEED_ONLY = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        NONE = JavaStaticField("Ljava/security/DrbgParameters$Capability;")

    class NextBytes(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$NextBytes"
        getStrength = JavaMethod("()I")
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")

    class Reseed(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Reseed"
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")

class AlgorithmParametersSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParametersSpi"
    __javaconstructor__ = [("()V", False)]

class Permissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Permissions"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(Ljava/security/Permission;)V")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    implies = JavaMethod("(Ljava/security/Permission;)Z")

class PrivilegedAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedAction"
    run = JavaMethod("()Ljava/lang/Object;")

class GeneralSecurityException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/GeneralSecurityException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class PrivilegedExceptionAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedExceptionAction"
    run = JavaMethod("()Ljava/lang/Object;")

class PolicySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PolicySpi"
    __javaconstructor__ = [("()V", False)]

class ProtectionDomain(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/ProtectionDomain"
    __javaconstructor__ = [("(Ljava/security/CodeSource;Ljava/security/PermissionCollection;)V", False), ("(Ljava/security/CodeSource;Ljava/security/PermissionCollection;Ljava/lang/ClassLoader;[Ljava/security/Principal;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getClassLoader = JavaMethod("()Ljava/lang/ClassLoader;")
    getCodeSource = JavaMethod("()Ljava/security/CodeSource;")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getPermissions = JavaMethod("()Ljava/security/PermissionCollection;")
    getPrincipals = JavaMethod("()[Ljava/security/Principal;")
    staticPermissionsOnly = JavaMethod("()Z")

class DigestInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/security/MessageDigest;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    on = JavaMethod("(Z)V")
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")

class UnrecoverableEntryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnrecoverableEntryException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Key(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Key"
    serialVersionUID = JavaStaticField("J")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class MessageDigestSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigestSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")

class DigestException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class AccessControlException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessControlException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/Permission;)V", False)]
    getPermission = JavaMethod("()Ljava/security/Permission;")

class KeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyFactorySpi"
    __javaconstructor__ = [("()V", False)]

class KeyManagementException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyManagementException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class Identity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Identity"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False), ("(Ljava/lang/String;)V", False)]
    certificates = JavaMethod("()[Ljava/security/Certificate;")
    getInfo = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("(Z)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])
    hashCode = JavaMethod("()I")
    getScope = JavaMethod("()Ljava/security/IdentityScope;")
    setPublicKey = JavaMethod("(Ljava/security/PublicKey;)V")
    setInfo = JavaMethod("(Ljava/lang/String;)V")
    addCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    removeCertificate = JavaMethod("(Ljava/security/Certificate;)V")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")

class KeyRep(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyRep"
    __javaconstructor__ = [("(Ljava/security/KeyRep$Type;Ljava/lang/String;Ljava/lang/String;[B)V", False)]

    class Type(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyRep$Type"
        SECRET = JavaStaticField("Ljava/security/KeyRep$Type;")
        PUBLIC = JavaStaticField("Ljava/security/KeyRep$Type;")
        PRIVATE = JavaStaticField("Ljava/security/KeyRep$Type;")
        values = JavaStaticMethod("()[Ljava/security/KeyRep$Type;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/KeyRep$Type;")
        SECRET = JavaStaticField("Ljava/security/KeyRep$Type;")
        PUBLIC = JavaStaticField("Ljava/security/KeyRep$Type;")
        PRIVATE = JavaStaticField("Ljava/security/KeyRep$Type;")

class AlgorithmParameterGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGenerator"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameterGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameterGenerator;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(I)V", False, False)])
    generateParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")

class DomainCombiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DomainCombiner"
    combine = JavaMethod("([Ljava/security/ProtectionDomain;[Ljava/security/ProtectionDomain;)[Ljava/security/ProtectionDomain;")

class GuardedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/GuardedObject"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/security/Guard;)V", False)]
    getObject = JavaMethod("()Ljava/lang/Object;")

class BasicPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/BasicPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")

class NoSuchProviderException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/NoSuchProviderException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class PrivilegedActionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivilegedActionException"
    __javaconstructor__ = [("(Ljava/lang/Exception;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")

class Permission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Permission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")

class AlgorithmParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameters"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getParameterSpec = JavaMethod("(Ljava/lang/Class;)Ljava/security/spec/AlgorithmParameterSpec;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/AlgorithmParameters;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/AlgorithmParameters;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("([BLjava/lang/String;)V", False, False), ("([B)V", False, False)])
    getEncoded = JavaMultipleMethod([("()[B", False, False), ("(Ljava/lang/String;)[B", False, False)])

class CryptoPrimitive(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CryptoPrimitive"
    MESSAGE_DIGEST = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SECURE_RANDOM = JavaStaticField("Ljava/security/CryptoPrimitive;")
    BLOCK_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    STREAM_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    MAC = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_WRAP = JavaStaticField("Ljava/security/CryptoPrimitive;")
    PUBLIC_KEY_ENCRYPTION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SIGNATURE = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_ENCAPSULATION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_AGREEMENT = JavaStaticField("Ljava/security/CryptoPrimitive;")
    values = JavaStaticMethod("()[Ljava/security/CryptoPrimitive;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/CryptoPrimitive;")
    MESSAGE_DIGEST = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SECURE_RANDOM = JavaStaticField("Ljava/security/CryptoPrimitive;")
    BLOCK_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    STREAM_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    MAC = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_WRAP = JavaStaticField("Ljava/security/CryptoPrimitive;")
    PUBLIC_KEY_ENCRYPTION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SIGNATURE = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_ENCAPSULATION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_AGREEMENT = JavaStaticField("Ljava/security/CryptoPrimitive;")

class Policy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Policy"
    __javaconstructor__ = [("()V", False)]
    UNSUPPORTED_EMPTY_COLLECTION = JavaStaticField("Ljava/security/PermissionCollection;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Policy$Parameters;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/lang/String;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/security/Provider;)Ljava/security/Policy;", True, False)])
    implies = JavaMethod("(Ljava/security/ProtectionDomain;Ljava/security/Permission;)Z")
    getPermissions = JavaMultipleMethod([("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;", False, False), ("(Ljava/security/ProtectionDomain;)Ljava/security/PermissionCollection;", False, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    getPolicy = JavaStaticMethod("()Ljava/security/Policy;")
    getParameters = JavaMethod("()Ljava/security/Policy$Parameters;")
    refresh = JavaMethod("()V")
    setPolicy = JavaStaticMethod("(Ljava/security/Policy;)V")

    class Parameters(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Policy$Parameters"

class MessageDigest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/MessageDigest"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("([BII)V", False, False), ("(B)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/MessageDigest;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/MessageDigest;", True, False)])
    isEqual = JavaStaticMethod("([B[B)Z")
    getDigestLength = JavaMethod("()I")
    digest = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False), ("([B)[B", False, False)])

class KeyStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStoreException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class AlgorithmConstraints(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmConstraints"
    permits = JavaMultipleMethod([("(Ljava/util/Set;Ljava/lang/String;Ljava/security/AlgorithmParameters;)Z", False, False), ("(Ljava/util/Set;Ljava/security/Key;)Z", False, False), ("(Ljava/util/Set;Ljava/lang/String;Ljava/security/Key;Ljava/security/AlgorithmParameters;)Z", False, False)])

class SecureRandomSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandomSpi"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")

class SignedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignedObject"
    __javaconstructor__ = [("(Ljava/io/Serializable;Ljava/security/PrivateKey;Ljava/security/Signature;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getSignature = JavaMethod("()[B")
    getObject = JavaMethod("()Ljava/lang/Object;")
    verify = JavaMethod("(Ljava/security/PublicKey;Ljava/security/Signature;)Z")

class NoSuchAlgorithmException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/NoSuchAlgorithmException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class AlgorithmParameterGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGeneratorSpi"
    __javaconstructor__ = [("()V", False)]

class InvalidAlgorithmParameterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidAlgorithmParameterException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class SecureClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureClassLoader"

class AllPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AllPermission"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")

class UnresolvedPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnresolvedPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/security/cert/Certificate;)V", False)]
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")
    getUnresolvedType = JavaMethod("()Ljava/lang/String;")
    getUnresolvedName = JavaMethod("()Ljava/lang/String;")
    getUnresolvedActions = JavaMethod("()Ljava/lang/String;")
    getUnresolvedCerts = JavaMethod("()[Ljava/security/cert/Certificate;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")

class KeyStoreSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStoreSpi"
    __javaconstructor__ = [("()V", False)]
    engineGetAttributes = JavaMethod("(Ljava/lang/String;)Ljava/util/Set;")
    engineGetKey = JavaMethod("(Ljava/lang/String;[C)Ljava/security/Key;")
    engineGetCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/Certificate;")
    engineGetCertificate = JavaMethod("(Ljava/lang/String;)Ljava/security/cert/Certificate;")
    engineGetCreationDate = JavaMethod("(Ljava/lang/String;)Ljava/util/Date;")
    engineSetKeyEntry = JavaMultipleMethod([("(Ljava/lang/String;[B[Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/lang/String;Ljava/security/Key;[C[Ljava/security/cert/Certificate;)V", False, False)])
    engineSetCertificateEntry = JavaMethod("(Ljava/lang/String;Ljava/security/cert/Certificate;)V")
    engineDeleteEntry = JavaMethod("(Ljava/lang/String;)V")
    engineAliases = JavaMethod("()Ljava/util/Enumeration;")
    engineContainsAlias = JavaMethod("(Ljava/lang/String;)Z")
    engineSize = JavaMethod("()I")
    engineIsKeyEntry = JavaMethod("(Ljava/lang/String;)Z")
    engineIsCertificateEntry = JavaMethod("(Ljava/lang/String;)Z")
    engineGetCertificateAlias = JavaMethod("(Ljava/security/cert/Certificate;)Ljava/lang/String;")
    engineStore = JavaMultipleMethod([("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False), ("(Ljava/io/OutputStream;[C)V", False, False)])
    engineLoad = JavaMultipleMethod([("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False), ("(Ljava/io/InputStream;[C)V", False, False)])
    engineGetEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Entry;")
    engineSetEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$Entry;Ljava/security/KeyStore$ProtectionParameter;)V")
    engineEntryInstanceOf = JavaMethod("(Ljava/lang/String;Ljava/lang/Class;)Z")
    engineProbe = JavaMethod("(Ljava/io/InputStream;)Z")

class CodeSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CodeSource"
    __javaconstructor__ = [("(Ljava/net/URL;[Ljava/security/cert/Certificate;)V", False), ("(Ljava/net/URL;[Ljava/security/CodeSigner;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLocation = JavaMethod("()Ljava/net/URL;")
    getCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    implies = JavaMethod("(Ljava/security/CodeSource;)Z")
    getCodeSigners = JavaMethod("()[Ljava/security/CodeSigner;")

class AccessController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessController"
    checkPermission = JavaStaticMethod("(Ljava/security/Permission;)V")
    doPrivileged = JavaMultipleMethod([("(Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;[Ljava/security/Permission;)Ljava/lang/Object;", True, True), ("(Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;[Ljava/security/Permission;)Ljava/lang/Object;", True, True)])
    getContext = JavaStaticMethod("()Ljava/security/AccessControlContext;")
    doPrivilegedWithCombiner = JavaMultipleMethod([("(Ljava/security/PrivilegedExceptionAction;Ljava/security/AccessControlContext;[Ljava/security/Permission;)Ljava/lang/Object;", True, True), ("(Ljava/security/PrivilegedAction;Ljava/security/AccessControlContext;[Ljava/security/Permission;)Ljava/lang/Object;", True, True), ("(Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;", True, False), ("(Ljava/security/PrivilegedAction;)Ljava/lang/Object;", True, False)])

class InvalidParameterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidParameterException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Timestamp"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CertPath;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignerCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    getTimestamp = JavaMethod("()Ljava/util/Date;")

class IdentityScope(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/IdentityScope"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False)]
    getIdentity = JavaMultipleMethod([("(Ljava/security/PublicKey;)Ljava/security/Identity;", False, False), ("(Ljava/security/Principal;)Ljava/security/Identity;", False, False), ("(Ljava/lang/String;)Ljava/security/Identity;", False, False)])
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    addIdentity = JavaMethod("(Ljava/security/Identity;)V")
    getSystemScope = JavaStaticMethod("()Ljava/security/IdentityScope;")
    removeIdentity = JavaMethod("(Ljava/security/Identity;)V")
    identities = JavaMethod("()Ljava/util/Enumeration;")

class Security(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Security"
    getProviders = JavaMultipleMethod([("(Ljava/lang/String;)[Ljava/security/Provider;", True, False), ("()[Ljava/security/Provider;", True, False), ("(Ljava/util/Map;)[Ljava/security/Provider;", True, False)])
    removeProvider = JavaStaticMethod("(Ljava/lang/String;)V")
    getProvider = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/Provider;")
    getProperty = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addProvider = JavaStaticMethod("(Ljava/security/Provider;)I")
    insertProviderAt = JavaStaticMethod("(Ljava/security/Provider;I)I")
    getAlgorithmProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getAlgorithms = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Set;")

class KeyPairGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPairGenerator"
    generateKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyPairGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyPairGenerator;", True, False)])
    initialize = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False)])
    genKeyPair = JavaMethod("()Ljava/security/KeyPair;")

class DigestOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/security/MessageDigest;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    on = JavaMethod("(Z)V")
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")

class ProviderException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/ProviderException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Certificate"
    toString = JavaMethod("(Z)Ljava/lang/String;")
    decode = JavaMethod("(Ljava/io/InputStream;)V")
    encode = JavaMethod("(Ljava/io/OutputStream;)V")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getPrincipal = JavaMethod("()Ljava/security/Principal;")
    getGuarantor = JavaMethod("()Ljava/security/Principal;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")

class SignatureException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignatureException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class KeyStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStore"
    getCertificate = JavaMethod("(Ljava/lang/String;)Ljava/security/cert/Certificate;")
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    size = JavaMethod("()I")
    load = JavaMultipleMethod([("(Ljava/io/InputStream;[C)V", False, False), ("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False)])
    store = JavaMultipleMethod([("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False), ("(Ljava/io/OutputStream;[C)V", False, False)])
    getKey = JavaMethod("(Ljava/lang/String;[C)Ljava/security/Key;")
    getInstance = JavaMultipleMethod([("(Ljava/io/File;[C)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyStore;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$LoadStoreParameter;)Ljava/security/KeyStore;", True, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    isCertificateEntry = JavaMethod("(Ljava/lang/String;)Z")
    getCreationDate = JavaMethod("(Ljava/lang/String;)Ljava/util/Date;")
    setKeyEntry = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Key;[C[Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/lang/String;[B[Ljava/security/cert/Certificate;)V", False, False)])
    setCertificateEntry = JavaMethod("(Ljava/lang/String;Ljava/security/cert/Certificate;)V")
    containsAlias = JavaMethod("(Ljava/lang/String;)Z")
    isKeyEntry = JavaMethod("(Ljava/lang/String;)Z")
    getCertificateAlias = JavaMethod("(Ljava/security/cert/Certificate;)Ljava/lang/String;")
    setEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$Entry;Ljava/security/KeyStore$ProtectionParameter;)V")
    entryInstanceOf = JavaMethod("(Ljava/lang/String;Ljava/lang/Class;)Z")
    getEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Entry;")
    aliases = JavaMethod("()Ljava/util/Enumeration;")
    getAttributes = JavaMethod("(Ljava/lang/String;)Ljava/util/Set;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/Certificate;")
    deleteEntry = JavaMethod("(Ljava/lang/String;)V")

    class LoadStoreParameter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$LoadStoreParameter"
        getProtectionParameter = JavaMethod("()Ljava/security/KeyStore$ProtectionParameter;")

    class ProtectionParameter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$ProtectionParameter"

    class Entry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$Entry"
        getAttributes = JavaMethod("()Ljava/util/Set;")

        class Attribute(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "java/security/KeyStore$Entry$Attribute"
            getName = JavaMethod("()Ljava/lang/String;")
            getValue = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$Builder"
        newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/security/KeyStore;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False)])
        getProtectionParameter = JavaMethod("(Ljava/lang/String;)Ljava/security/KeyStore$ProtectionParameter;")
        getKeyStore = JavaMethod("()Ljava/security/KeyStore;")

    class TrustedCertificateEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$TrustedCertificateEntry"
        __javaconstructor__ = [("(Ljava/security/cert/Certificate;)V", False), ("(Ljava/security/cert/Certificate;Ljava/util/Set;)V", False)]
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        getTrustedCertificate = JavaMethod("()Ljava/security/cert/Certificate;")

    class SecretKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$SecretKeyEntry"
        __javaconstructor__ = [("(Ljavax/crypto/SecretKey;)V", False), ("(Ljavax/crypto/SecretKey;Ljava/util/Set;)V", False)]
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        getSecretKey = JavaMethod("()Ljavax/crypto/SecretKey;")

    class PrivateKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$PrivateKeyEntry"
        __javaconstructor__ = [("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;Ljava/util/Set;)V", False), ("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;)V", False)]
        getCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
        getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        getCertificateChain = JavaMethod("()[Ljava/security/cert/Certificate;")

    class CallbackHandlerProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$CallbackHandlerProtection"
        __javaconstructor__ = [("(Ljavax/security/auth/callback/CallbackHandler;)V", False)]
        getCallbackHandler = JavaMethod("()Ljavax/security/auth/callback/CallbackHandler;")

    class PasswordProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$PasswordProtection"
        __javaconstructor__ = [("([C)V", False), ("([CLjava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
        getPassword = JavaMethod("()[C")
        getProtectionParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
        isDestroyed = JavaMethod("()Z")
        destroy = JavaMethod("()V")
        getProtectionAlgorithm = JavaMethod("()Ljava/lang/String;")

class InvalidKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidKeyException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class CodeSigner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CodeSigner"
    __javaconstructor__ = [("(Ljava/security/cert/CertPath;Ljava/security/Timestamp;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignerCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    getTimestamp = JavaMethod("()Ljava/security/Timestamp;")

class Principal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Principal"
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljavax/security/auth/Subject;)Z")

class Guard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Guard"
    checkGuard = JavaMethod("(Ljava/lang/Object;)V")

class PublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")

class DomainLoadStoreParameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DomainLoadStoreParameter"
    __javaconstructor__ = [("(Ljava/net/URI;Ljava/util/Map;)V", False)]
    getProtectionParams = JavaMethod("()Ljava/util/Map;")
    getConfiguration = JavaMethod("()Ljava/net/URI;")
    getProtectionParameter = JavaMethod("()Ljava/security/KeyStore$ProtectionParameter;")

class KeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class SecurityPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecurityPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]

class PermissionCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PermissionCollection"
    __javaconstructor__ = [("()V", False)]
    elementsAsStream = JavaMethod("()Ljava/util/stream/Stream;")
    toString = JavaMethod("()Ljava/lang/String;")
    add = JavaMethod("(Ljava/security/Permission;)V")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    setReadOnly = JavaMethod("()V")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    isReadOnly = JavaMethod("()Z")

class SecureRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandom"
    __javaconstructor__ = [("()V", False), ("([B)V", False)]
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False)])
    getParameters = JavaMethod("()Ljava/security/SecureRandomParameters;")
    nextBytes = JavaMultipleMethod([("([B)V", False, False), ("([BLjava/security/SecureRandomParameters;)V", False, False)])
    generateSeed = JavaMethod("(I)[B")
    getInstanceStrong = JavaStaticMethod("()Ljava/security/SecureRandom;")
    reseed = JavaMultipleMethod([("(Ljava/security/SecureRandomParameters;)V", False, False), ("()V", False, False)])
    getSeed = JavaStaticMethod("(I)[B")
    setSeed = JavaMultipleMethod([("([B)V", False, False), ("(J)V", False, False)])

class Signature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signature"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    initVerify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/cert/Certificate;)V", False, False)])
    initSign = JavaMultipleMethod([("(Ljava/security/PrivateKey;Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/PrivateKey;)V", False, False)])
    setParameter = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)V", False, False)])
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([BII)V", False, False), ("(B)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/Signature;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/Signature;", True, False)])
    sign = JavaMultipleMethod([("([BII)I", False, False), ("()[B", False, False)])
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    verify = JavaMultipleMethod([("([BII)Z", False, False), ("([B)Z", False, False)])

class KeyPair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPair"
    __javaconstructor__ = [("(Ljava/security/PublicKey;Ljava/security/PrivateKey;)V", False)]
    getPublic = JavaMethod("()Ljava/security/PublicKey;")
    getPrivate = JavaMethod("()Ljava/security/PrivateKey;")

class SecureRandomParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandomParameters"

class KeyPairGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyPairGeneratorSpi"
    __javaconstructor__ = [("()V", False)]
    generateKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    initialize = JavaMultipleMethod([("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False)])

class PrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")

class AuthProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AuthProvider"
    login = JavaMethod("(Ljavax/security/auth/Subject;Ljavax/security/auth/callback/CallbackHandler;)V")
    logout = JavaMethod("()V")
    setCallbackHandler = JavaMethod("(Ljavax/security/auth/callback/CallbackHandler;)V")

class Signer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Signer"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False), ("(Ljava/lang/String;)V", False)]
    getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    setKeyPair = JavaMethod("(Ljava/security/KeyPair;)V")
    toString = JavaMethod("()Ljava/lang/String;")

class UnrecoverableKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/UnrecoverableKeyException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]