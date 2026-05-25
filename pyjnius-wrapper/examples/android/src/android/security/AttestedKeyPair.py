from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttestedKeyPair"]

class AttestedKeyPair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/AttestedKeyPair"
    __javaconstructor__ = [("(Ljava/security/KeyPair;Ljava/util/List;)V", False)]
    getKeyPair = JavaMethod("()Ljava/security/KeyPair;")
    getAttestationRecord = JavaMethod("()Ljava/util/List;")