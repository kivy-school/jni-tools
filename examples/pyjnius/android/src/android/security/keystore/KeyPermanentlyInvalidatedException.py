from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPermanentlyInvalidatedException"]

class KeyPermanentlyInvalidatedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyPermanentlyInvalidatedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]