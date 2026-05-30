from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SNIServerName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIServerName"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")

class SSLKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLKeyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class SSLSessionBindingListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionBindingListener"
    valueBound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")
    valueUnbound = JavaMethod("(Ljavax/net/ssl/SSLSessionBindingEvent;)V")

class ManagerFactoryParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/ManagerFactoryParameters"

class SSLSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSession"
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getCreationTime = JavaMethod("()J")
    getPeerHost = JavaMethod("()Ljava/lang/String;")
    getPeerPort = JavaMethod("()I")
    getSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getLastAccessedTime = JavaMethod("()J")
    removeValue = JavaMethod("(Ljava/lang/String;)V")
    getValueNames = JavaMethod("()[Ljava/lang/String;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getPacketBufferSize = JavaMethod("()I")
    getApplicationBufferSize = JavaMethod("()I")
    getValue = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getId = JavaMethod("()[B")
    invalidate = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    putValue = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")

class SSLSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocketFactory"
    __javaconstructor__ = [("()V", False)]
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    createSocket = JavaMultipleMethod([("(Ljava/net/Socket;Ljava/io/InputStream;Z)Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False)])
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getDefault = JavaStaticMethod("()Ljavax/net/SocketFactory;")

class StandardConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/StandardConstants"
    SNI_HOST_NAME = JavaStaticField("I")

class KeyManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/KeyManagerFactory;", True, False), ("(Ljava/lang/String;)Ljavax/net/ssl/KeyManagerFactory;", True, False)])
    init = JavaMultipleMethod([("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False), ("(Ljava/security/KeyStore;[C)V", False, False)])
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getKeyManagers = JavaMethod("()[Ljavax/net/ssl/KeyManager;")

class SSLContextSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContextSpi"
    __javaconstructor__ = [("()V", False)]

class X509ExtendedKeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509ExtendedKeyManager"
    chooseEngineClientAlias = JavaMethod("([Ljava/lang/String;[Ljava/security/Principal;Ljavax/net/ssl/SSLEngine;)Ljava/lang/String;")
    chooseEngineServerAlias = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;Ljavax/net/ssl/SSLEngine;)Ljava/lang/String;")

class SSLEngineResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLEngineResult"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLEngineResult$Status;Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;II)V", False), ("(Ljavax/net/ssl/SSLEngineResult$Status;Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;IIJ)V", False)]
    getStatus = JavaMethod("()Ljavax/net/ssl/SSLEngineResult$Status;")
    getHandshakeStatus = JavaMethod("()Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
    toString = JavaMethod("()Ljava/lang/String;")
    sequenceNumber = JavaMethod("()J")
    bytesConsumed = JavaMethod("()I")
    bytesProduced = JavaMethod("()I")

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/net/ssl/SSLEngineResult$Status"
        BUFFER_UNDERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        BUFFER_OVERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        OK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        CLOSED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        values = JavaStaticMethod("()[Ljavax/net/ssl/SSLEngineResult$Status;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SSLEngineResult$Status;")
        BUFFER_UNDERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        BUFFER_OVERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        OK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")
        CLOSED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$Status;")

    class HandshakeStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/net/ssl/SSLEngineResult$HandshakeStatus"
        NOT_HANDSHAKING = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        FINISHED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_TASK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_WRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_UNWRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_UNWRAP_AGAIN = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        values = JavaStaticMethod("()[Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NOT_HANDSHAKING = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        FINISHED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_TASK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_WRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_UNWRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NEED_UNWRAP_AGAIN = JavaStaticField("Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")

class SSLPeerUnverifiedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLPeerUnverifiedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class SSLPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLPermission"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]

class SSLHandshakeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLHandshakeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class TrustManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]

class SSLProtocolException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLProtocolException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]

class SSLServerSocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocketFactory"
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getDefault = JavaStaticMethod("()Ljavax/net/ServerSocketFactory;")

class CertPathTrustManagerParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/CertPathTrustManagerParameters"
    __javaconstructor__ = [("(Ljava/security/cert/CertPathParameters;)V", False)]
    getParameters = JavaMethod("()Ljava/security/cert/CertPathParameters;")

class SNIMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIMatcher"
    matches = JavaMethod("(Ljavax/net/ssl/SNIServerName;)Z")
    getType = JavaMethod("()I")

class SSLSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSocket"
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    getHandshakeApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    setHandshakeApplicationProtocolSelector = JavaMethod("(Ljava/util/function/BiFunction;)V")
    getHandshakeApplicationProtocolSelector = JavaMethod("()Ljava/util/function/BiFunction;")
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    getHandshakeSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    addHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    removeHandshakeCompletedListener = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedListener;)V")
    startHandshake = JavaMethod("()V")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")

class SSLParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLParameters"
    __javaconstructor__ = [("([Ljava/lang/String;[Ljava/lang/String;)V", False), ("([Ljava/lang/String;)V", False), ("()V", False)]
    getAlgorithmConstraints = JavaMethod("()Ljava/security/AlgorithmConstraints;")
    setAlgorithmConstraints = JavaMethod("(Ljava/security/AlgorithmConstraints;)V")
    getEndpointIdentificationAlgorithm = JavaMethod("()Ljava/lang/String;")
    setEndpointIdentificationAlgorithm = JavaMethod("(Ljava/lang/String;)V")
    setServerNames = JavaMethod("(Ljava/util/List;)V")
    getServerNames = JavaMethod("()Ljava/util/List;")
    setSNIMatchers = JavaMethod("(Ljava/util/Collection;)V")
    getSNIMatchers = JavaMethod("()Ljava/util/Collection;")
    setUseCipherSuitesOrder = JavaMethod("(Z)V")
    getUseCipherSuitesOrder = JavaMethod("()Z")
    setEnableRetransmissions = JavaMethod("(Z)V")
    getEnableRetransmissions = JavaMethod("()Z")
    setMaximumPacketSize = JavaMethod("(I)V")
    getMaximumPacketSize = JavaMethod("()I")
    getApplicationProtocols = JavaMethod("()[Ljava/lang/String;")
    setApplicationProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSignatureSchemes = JavaMethod("()[Ljava/lang/String;")
    setSignatureSchemes = JavaMethod("([Ljava/lang/String;)V")
    getNamedGroups = JavaMethod("()[Ljava/lang/String;")
    setNamedGroups = JavaMethod("([Ljava/lang/String;)V")
    setCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    setProtocols = JavaMethod("([Ljava/lang/String;)V")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    getCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getProtocols = JavaMethod("()[Ljava/lang/String;")

class X509KeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509KeyManager"
    getPrivateKey = JavaMethod("(Ljava/lang/String;)Ljava/security/PrivateKey;")
    getClientAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseClientAlias = JavaMethod("([Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")
    getServerAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseServerAlias = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")

class KeyManagerFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManagerFactorySpi"
    __javaconstructor__ = [("()V", False)]

class X509TrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509TrustManager"
    checkServerTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    checkClientTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    getAcceptedIssuers = JavaMethod("()[Ljava/security/cert/X509Certificate;")

class TrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManager"

class ExtendedSSLSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/ExtendedSSLSession"
    __javaconstructor__ = [("()V", False)]
    getLocalSupportedSignatureAlgorithms = JavaMethod("()[Ljava/lang/String;")
    getPeerSupportedSignatureAlgorithms = JavaMethod("()[Ljava/lang/String;")
    getRequestedServerNames = JavaMethod("()Ljava/util/List;")
    getStatusResponses = JavaMethod("()Ljava/util/List;")

class HttpsURLConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HttpsURLConnection"
    HTTP_OK = JavaStaticField("I")
    HTTP_CREATED = JavaStaticField("I")
    HTTP_ACCEPTED = JavaStaticField("I")
    HTTP_NOT_AUTHORITATIVE = JavaStaticField("I")
    HTTP_NO_CONTENT = JavaStaticField("I")
    HTTP_RESET = JavaStaticField("I")
    HTTP_PARTIAL = JavaStaticField("I")
    HTTP_MULT_CHOICE = JavaStaticField("I")
    HTTP_MOVED_PERM = JavaStaticField("I")
    HTTP_MOVED_TEMP = JavaStaticField("I")
    HTTP_SEE_OTHER = JavaStaticField("I")
    HTTP_NOT_MODIFIED = JavaStaticField("I")
    HTTP_USE_PROXY = JavaStaticField("I")
    HTTP_BAD_REQUEST = JavaStaticField("I")
    HTTP_UNAUTHORIZED = JavaStaticField("I")
    HTTP_PAYMENT_REQUIRED = JavaStaticField("I")
    HTTP_FORBIDDEN = JavaStaticField("I")
    HTTP_NOT_FOUND = JavaStaticField("I")
    HTTP_BAD_METHOD = JavaStaticField("I")
    HTTP_NOT_ACCEPTABLE = JavaStaticField("I")
    HTTP_PROXY_AUTH = JavaStaticField("I")
    HTTP_CLIENT_TIMEOUT = JavaStaticField("I")
    HTTP_CONFLICT = JavaStaticField("I")
    HTTP_GONE = JavaStaticField("I")
    HTTP_LENGTH_REQUIRED = JavaStaticField("I")
    HTTP_PRECON_FAILED = JavaStaticField("I")
    HTTP_ENTITY_TOO_LARGE = JavaStaticField("I")
    HTTP_REQ_TOO_LONG = JavaStaticField("I")
    HTTP_UNSUPPORTED_TYPE = JavaStaticField("I")
    HTTP_SERVER_ERROR = JavaStaticField("I")
    HTTP_INTERNAL_ERROR = JavaStaticField("I")
    HTTP_NOT_IMPLEMENTED = JavaStaticField("I")
    HTTP_BAD_GATEWAY = JavaStaticField("I")
    HTTP_UNAVAILABLE = JavaStaticField("I")
    HTTP_GATEWAY_TIMEOUT = JavaStaticField("I")
    HTTP_VERSION = JavaStaticField("I")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getDefaultSSLSocketFactory = JavaStaticMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    getServerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    setHostnameVerifier = JavaMethod("(Ljavax/net/ssl/HostnameVerifier;)V")
    setDefaultHostnameVerifier = JavaStaticMethod("(Ljavax/net/ssl/HostnameVerifier;)V")
    getDefaultHostnameVerifier = JavaStaticMethod("()Ljavax/net/ssl/HostnameVerifier;")
    getHostnameVerifier = JavaMethod("()Ljavax/net/ssl/HostnameVerifier;")
    setDefaultSSLSocketFactory = JavaStaticMethod("(Ljavax/net/ssl/SSLSocketFactory;)V")
    setSSLSocketFactory = JavaMethod("(Ljavax/net/ssl/SSLSocketFactory;)V")
    getSSLSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")
    getSSLSession = JavaMethod("()Ljava/util/Optional;")

class SSLException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class SSLServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLServerSocket"
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")

class HandshakeCompletedEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedEvent"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSocket;Ljavax/net/ssl/SSLSession;)V", False)]
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getCipherSuite = JavaMethod("()Ljava/lang/String;")
    getPeerCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getLocalCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getPeerCertificateChain = JavaMethod("()[Ljavax/security/cert/X509Certificate;")
    getSocket = JavaMethod("()Ljavax/net/ssl/SSLSocket;")
    getPeerPrincipal = JavaMethod("()Ljava/security/Principal;")
    getLocalPrincipal = JavaMethod("()Ljava/security/Principal;")

class SSLEngine(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLEngine"
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    getHandshakeApplicationProtocol = JavaMethod("()Ljava/lang/String;")
    setHandshakeApplicationProtocolSelector = JavaMethod("(Ljava/util/function/BiFunction;)V")
    getHandshakeApplicationProtocolSelector = JavaMethod("()Ljava/util/function/BiFunction;")
    getPeerHost = JavaMethod("()Ljava/lang/String;")
    getPeerPort = JavaMethod("()I")
    getDelegatedTask = JavaMethod("()Ljava/lang/Runnable;")
    closeInbound = JavaMethod("()V")
    isInboundDone = JavaMethod("()Z")
    closeOutbound = JavaMethod("()V")
    isOutboundDone = JavaMethod("()Z")
    beginHandshake = JavaMethod("()V")
    getHandshakeStatus = JavaMethod("()Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
    wrap = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;IILjava/nio/ByteBuffer;)Ljavax/net/ssl/SSLEngineResult;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)Ljavax/net/ssl/SSLEngineResult;", False, False), ("([Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)Ljavax/net/ssl/SSLEngineResult;", False, False)])
    unwrap = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)Ljavax/net/ssl/SSLEngineResult;", False, False), ("(Ljava/nio/ByteBuffer;[Ljava/nio/ByteBuffer;)Ljavax/net/ssl/SSLEngineResult;", False, False), ("(Ljava/nio/ByteBuffer;[Ljava/nio/ByteBuffer;II)Ljavax/net/ssl/SSLEngineResult;", False, False)])
    getEnabledCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getEnabledProtocols = JavaMethod("()[Ljava/lang/String;")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    setEnabledCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    setEnabledProtocols = JavaMethod("([Ljava/lang/String;)V")
    getSupportedProtocols = JavaMethod("()[Ljava/lang/String;")
    getHandshakeSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    setUseClientMode = JavaMethod("(Z)V")
    getUseClientMode = JavaMethod("()Z")
    setEnableSessionCreation = JavaMethod("(Z)V")
    getEnableSessionCreation = JavaMethod("()Z")
    getSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setSSLParameters = JavaMethod("(Ljavax/net/ssl/SSLParameters;)V")

class HostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HostnameVerifier"
    verify = JavaMethod("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z")

class SSLContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContext"
    getSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getDefault = JavaStaticMethod("()Ljavax/net/ssl/SSLContext;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/SSLContext;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/SSLContext;", True, False)])
    init = JavaMethod("([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getServerSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLServerSocketFactory;")
    createSSLEngine = JavaMultipleMethod([("(Ljava/lang/String;I)Ljavax/net/ssl/SSLEngine;", False, False), ("()Ljavax/net/ssl/SSLEngine;", False, False)])
    getServerSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getClientSessionContext = JavaMethod("()Ljavax/net/ssl/SSLSessionContext;")
    getDefaultSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    getSupportedSSLParameters = JavaMethod("()Ljavax/net/ssl/SSLParameters;")
    setDefault = JavaStaticMethod("(Ljavax/net/ssl/SSLContext;)V")

class SSLSessionContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionContext"
    getIds = JavaMethod("()Ljava/util/Enumeration;")
    getSession = JavaMethod("([B)Ljavax/net/ssl/SSLSession;")
    setSessionTimeout = JavaMethod("(I)V")
    getSessionTimeout = JavaMethod("()I")
    setSessionCacheSize = JavaMethod("(I)V")
    getSessionCacheSize = JavaMethod("()I")

class KeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManager"

class TrustManagerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManagerFactory"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/net/ssl/TrustManagerFactory;", True, False), ("(Ljava/lang/String;)Ljavax/net/ssl/TrustManagerFactory;", True, False)])
    init = JavaMultipleMethod([("(Ljavax/net/ssl/ManagerFactoryParameters;)V", False, False), ("(Ljava/security/KeyStore;)V", False, False)])
    getDefaultAlgorithm = JavaStaticMethod("()Ljava/lang/String;")
    getTrustManagers = JavaMethod("()[Ljavax/net/ssl/TrustManager;")

class SNIHostName(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SNIHostName"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("([B)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAsciiName = JavaMethod("()Ljava/lang/String;")
    createSNIMatcher = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SNIMatcher;")

class HandshakeCompletedListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HandshakeCompletedListener"
    handshakeCompleted = JavaMethod("(Ljavax/net/ssl/HandshakeCompletedEvent;)V")

class SSLSessionBindingEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionBindingEvent"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSession;Ljava/lang/String;)V", False)]
    getSession = JavaMethod("()Ljavax/net/ssl/SSLSession;")
    getName = JavaMethod("()Ljava/lang/String;")

class X509ExtendedTrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509ExtendedTrustManager"
    __javaconstructor__ = [("()V", False)]
    checkServerTrusted = JavaMultipleMethod([("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljavax/net/ssl/SSLEngine;)V", False, False), ("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/net/Socket;)V", False, False)])
    checkClientTrusted = JavaMultipleMethod([("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/net/Socket;)V", False, False), ("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljavax/net/ssl/SSLEngine;)V", False, False)])

class KeyStoreBuilderParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyStoreBuilderParameters"
    __javaconstructor__ = [("(Ljava/security/KeyStore$Builder;)V", False), ("(Ljava/util/List;)V", False)]
    getParameters = JavaMethod("()Ljava/util/List;")