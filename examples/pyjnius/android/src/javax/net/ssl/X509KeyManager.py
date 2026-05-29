from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509KeyManager"]

class X509KeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509KeyManager"
    getPrivateKey = JavaMethod("(Ljava/lang/String;)Ljava/security/PrivateKey;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")
    getClientAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseClientAlias = JavaMethod("([Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")
    getServerAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseServerAlias = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")