from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigestOutputStream"]

class DigestOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/security/MessageDigest;)V", False)]
    digest = JavaField("Ljava/security/MessageDigest;")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    on = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")