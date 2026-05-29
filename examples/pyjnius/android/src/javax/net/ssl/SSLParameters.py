from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLParameters"]

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