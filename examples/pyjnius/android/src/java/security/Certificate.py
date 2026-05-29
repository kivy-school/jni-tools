from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Certificate"
    toString = JavaMethod("(Z)Ljava/lang/String;")
    decode = JavaMethod("(Ljava/io/InputStream;)V")
    encode = JavaMethod("(Ljava/io/OutputStream;)V")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getPrincipal = JavaMethod("()Ljava/security/Principal;")
    getGuarantor = JavaMethod("()Ljava/security/Principal;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")