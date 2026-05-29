from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigestOutputStream"]

class DigestOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljava/security/MessageDigest;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    on = JavaMethod("(Z)V")
    write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False)])
    setMessageDigest = JavaMethod("(Ljava/security/MessageDigest;)V")
    getMessageDigest = JavaMethod("()Ljava/security/MessageDigest;")