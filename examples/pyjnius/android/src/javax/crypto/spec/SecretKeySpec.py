from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKeySpec"]

class SecretKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/SecretKeySpec"
    __javaconstructor__ = [("([BLjava/lang/String;)V", False), ("([BIILjava/lang/String;)V", False)]
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")