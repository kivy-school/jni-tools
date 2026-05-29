from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NullCipher"]

class NullCipher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/NullCipher"
    __javaconstructor__ = [("()V", False)]
    ENCRYPT_MODE = JavaStaticField("I")
    DECRYPT_MODE = JavaStaticField("I")
    WRAP_MODE = JavaStaticField("I")
    UNWRAP_MODE = JavaStaticField("I")
    PUBLIC_KEY = JavaStaticField("I")
    PRIVATE_KEY = JavaStaticField("I")
    SECRET_KEY = JavaStaticField("I")