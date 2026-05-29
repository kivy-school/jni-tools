from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HpkeSpi"]

class HpkeSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/HpkeSpi"
    engineSeal = JavaMethod("([B[B)[B")
    engineOpen = JavaMethod("([B[B)[B")
    engineExport = JavaMethod("(I[B)[B")
    engineInitSenderWithSeed = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B[B)V")
    engineInitRecipient = JavaMethod("([BLjava/security/PrivateKey;[BLjava/security/PublicKey;[B[B)V")
    engineInitSender = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B)V")
    getEncapsulated = JavaMethod("()[B")