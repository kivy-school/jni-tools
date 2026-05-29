from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherOutputStream"]

class CipherOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljavax/crypto/Cipher;)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(I)V", False, False)])