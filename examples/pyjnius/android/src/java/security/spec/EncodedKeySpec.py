from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncodedKeySpec"]

class EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BLjava/lang/String;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    getFormat = JavaMethod("()Ljava/lang/String;")