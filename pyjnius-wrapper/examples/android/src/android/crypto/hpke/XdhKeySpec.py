from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XdhKeySpec"]

class XdhKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/XdhKeySpec"
    __javaconstructor__ = [("([B)V", False)]
    getFormat = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")