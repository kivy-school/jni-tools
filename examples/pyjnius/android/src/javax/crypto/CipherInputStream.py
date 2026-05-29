from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherInputStream"]

class CipherInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljavax/crypto/Cipher;)V", False)]
    close = JavaMethod("()V")
    read = JavaMultipleMethod([("([BII)I", False, False), ("([B)I", False, False), ("()I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")