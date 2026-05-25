from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Certificate"
    getGuarantor = JavaMethod("()Ljava/security/Principal;")
    getPrincipal = JavaMethod("()Ljava/security/Principal;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    encode = JavaMethod("(Ljava/io/OutputStream;)V")
    decode = JavaMethod("(Ljava/io/InputStream;)V")
    getFormat = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("(Z)Ljava/lang/String;")