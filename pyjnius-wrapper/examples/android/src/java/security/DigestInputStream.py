from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigestInputStream"]

class DigestInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/security/MessageDigest;)V", False)]
    digest = JavaField("Ljava/security/MessageDigest;")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    on = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")