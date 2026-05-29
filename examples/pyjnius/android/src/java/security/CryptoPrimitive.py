from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CryptoPrimitive"]

class CryptoPrimitive(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CryptoPrimitive"
    MESSAGE_DIGEST = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SECURE_RANDOM = JavaStaticField("Ljava/security/CryptoPrimitive;")
    BLOCK_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    STREAM_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    MAC = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_WRAP = JavaStaticField("Ljava/security/CryptoPrimitive;")
    PUBLIC_KEY_ENCRYPTION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SIGNATURE = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_ENCAPSULATION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_AGREEMENT = JavaStaticField("Ljava/security/CryptoPrimitive;")
    values = JavaStaticMethod("()[Ljava/security/CryptoPrimitive;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/CryptoPrimitive;")
    MESSAGE_DIGEST = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SECURE_RANDOM = JavaStaticField("Ljava/security/CryptoPrimitive;")
    BLOCK_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    STREAM_CIPHER = JavaStaticField("Ljava/security/CryptoPrimitive;")
    MAC = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_WRAP = JavaStaticField("Ljava/security/CryptoPrimitive;")
    PUBLIC_KEY_ENCRYPTION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    SIGNATURE = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_ENCAPSULATION = JavaStaticField("Ljava/security/CryptoPrimitive;")
    KEY_AGREEMENT = JavaStaticField("Ljava/security/CryptoPrimitive;")