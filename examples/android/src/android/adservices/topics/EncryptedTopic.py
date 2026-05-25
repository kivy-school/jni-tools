from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncryptedTopic"]

class EncryptedTopic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/topics/EncryptedTopic"
    __javaconstructor__ = [("([BLjava/lang/String;[B)V", False)]
    getEncryptedTopic = JavaMethod("()[B")
    getKeyIdentifier = JavaMethod("()Ljava/lang/String;")
    getEncapsulatedKey = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")