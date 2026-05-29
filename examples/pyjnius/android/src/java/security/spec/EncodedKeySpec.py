from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncodedKeySpec"]

class EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False)]
    getEncoded = JavaMethod("()[B")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")