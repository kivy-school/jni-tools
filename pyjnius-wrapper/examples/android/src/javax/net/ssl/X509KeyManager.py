from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509KeyManager"]

class X509KeyManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509KeyManager"
    getClientAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseClientAlias = JavaMethod("([Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")
    getServerAliases = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;)[Ljava/lang/String;")
    chooseServerAlias = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;Ljava/net/Socket;)Ljava/lang/String;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")
    getPrivateKey = JavaMethod("(Ljava/lang/String;)Ljava/security/PrivateKey;")