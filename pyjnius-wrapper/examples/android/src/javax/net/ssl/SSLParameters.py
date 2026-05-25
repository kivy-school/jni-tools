from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLParameters"]

class SSLParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLParameters"
    __javaconstructor__ = [("()V", False), ("([Ljava/lang/String;)V", False), ("([Ljava/lang/String;[Ljava/lang/String;)V", False)]
    getCipherSuites = JavaMethod("()[Ljava/lang/String;")
    setCipherSuites = JavaMethod("([Ljava/lang/String;)V")
    getProtocols = JavaMethod("()[Ljava/lang/String;")
    setProtocols = JavaMethod("([Ljava/lang/String;)V")
    getWantClientAuth = JavaMethod("()Z")
    setWantClientAuth = JavaMethod("(Z)V")
    getNeedClientAuth = JavaMethod("()Z")
    setNeedClientAuth = JavaMethod("(Z)V")
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
    getApplicationProtocols = JavaMethod("()[Ljava/lang/String;")
    setApplicationProtocols = JavaMethod("([Ljava/lang/String;)V")