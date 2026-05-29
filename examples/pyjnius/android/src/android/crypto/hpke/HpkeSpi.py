from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HpkeSpi"]

class HpkeSpi(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/HpkeSpi"
    engineInitSender = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B)V")
    engineInitSenderWithSeed = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B[B)V")
    engineInitRecipient = JavaMethod("([BLjava/security/PrivateKey;[BLjava/security/PublicKey;[B[B)V")
    engineSeal = JavaMethod("([B[B)[B")
    engineOpen = JavaMethod("([B[B)[B")
    engineExport = JavaMethod("(I[B)[B")
    getEncapsulated = JavaMethod("()[B")