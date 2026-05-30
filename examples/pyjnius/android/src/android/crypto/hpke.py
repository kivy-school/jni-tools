from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class XdhKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/XdhKeySpec"
    __javaconstructor__ = [("([B)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getKey = JavaMethod("()[B")
    getFormat = JavaMethod("()Ljava/lang/String;")

class HpkeSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/HpkeSpi"
    engineInitSenderWithSeed = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B[B)V")
    engineInitRecipient = JavaMethod("([BLjava/security/PrivateKey;[BLjava/security/PublicKey;[B[B)V")
    engineExport = JavaMethod("(I[B)[B")
    engineInitSender = JavaMethod("(Ljava/security/PublicKey;[BLjava/security/PrivateKey;[B[B)V")
    engineOpen = JavaMethod("([B[B)[B")
    engineSeal = JavaMethod("([B[B)[B")
    getEncapsulated = JavaMethod("()[B")