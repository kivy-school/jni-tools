from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherOutputStream"]

class CipherOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljavax/crypto/Cipher;)V", False), ("(Ljava/io/OutputStream;)V", False)]
    write = JavaMultipleMethod([("(I)V", False, False), ("([B)V", False, False), ("([BII)V", False, False)])
    flush = JavaMethod("()V")
    close = JavaMethod("()V")