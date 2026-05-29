from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKCS8EncodedKeySpec"]

class PKCS8EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/PKCS8EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BLjava/lang/String;)V", False)]
    getEncoded = JavaMethod("()[B")
    getFormat = JavaMethod("()Ljava/lang/String;")