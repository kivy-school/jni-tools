from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CodeSource"]

class CodeSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CodeSource"
    __javaconstructor__ = [("(Ljava/net/URL;[Ljava/security/cert/Certificate;)V", False), ("(Ljava/net/URL;[Ljava/security/CodeSigner;)V", False)]
    getLocation = JavaMethod("()Ljava/net/URL;")
    getCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getCodeSigners = JavaMethod("()[Ljava/security/CodeSigner;")
    implies = JavaMethod("(Ljava/security/CodeSource;)Z")