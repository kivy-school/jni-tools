from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509ExtendedKeyManager"]

class X509ExtendedKeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509ExtendedKeyManager"
    chooseEngineClientAlias = JavaMethod("([Ljava/lang/String;[Ljava/security/Principal;Ljavax/net/ssl/SSLEngine;)Ljava/lang/String;")
    chooseEngineServerAlias = JavaMethod("(Ljava/lang/String;[Ljava/security/Principal;Ljavax/net/ssl/SSLEngine;)Ljava/lang/String;")