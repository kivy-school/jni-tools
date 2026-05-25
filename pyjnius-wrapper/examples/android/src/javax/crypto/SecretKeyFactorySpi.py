from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKeyFactorySpi"]

class SecretKeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactorySpi"
    __javaconstructor__ = [("()V", False)]
    engineGenerateSecret = JavaMethod("(Ljava/security/spec/KeySpec;)Ljavax/crypto/SecretKey;")
    engineGetKeySpec = JavaMethod("(Ljavax/crypto/SecretKey;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    engineTranslateKey = JavaMethod("(Ljavax/crypto/SecretKey;)Ljavax/crypto/SecretKey;")