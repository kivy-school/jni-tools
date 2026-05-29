from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigestInputStream"]

class DigestInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljava/security/MessageDigest;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    on = JavaMethod("(Z)V")
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False)])
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")