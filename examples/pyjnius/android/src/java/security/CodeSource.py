from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CodeSource"]

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