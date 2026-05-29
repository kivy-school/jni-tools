from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherInputStream"]

class CipherInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljavax/crypto/Cipher;)V", False), ("(Ljava/io/InputStream;)V", False)]
    read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    close = JavaMethod("()V")
    markSupported = JavaMethod("()Z")