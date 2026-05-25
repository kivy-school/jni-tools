from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtendedSSLSession"]

class ExtendedSSLSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/ExtendedSSLSession"
    __javaconstructor__ = [("()V", False)]
    getLocalSupportedSignatureAlgorithms = JavaMethod("()[Ljava/lang/String;")
    getPeerSupportedSignatureAlgorithms = JavaMethod("()[Ljava/lang/String;")
    getRequestedServerNames = JavaMethod("()Ljava/util/List;")