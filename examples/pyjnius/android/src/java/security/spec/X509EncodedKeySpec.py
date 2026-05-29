from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509EncodedKeySpec"]

class X509EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/X509EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BLjava/lang/String;)V", False)]
    getEncoded = JavaMethod("()[B")
    getFormat = JavaMethod("()Ljava/lang/String;")