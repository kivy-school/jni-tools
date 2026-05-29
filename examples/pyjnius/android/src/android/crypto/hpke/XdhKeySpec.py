from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XdhKeySpec"]

class XdhKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/crypto/hpke/XdhKeySpec"
    __javaconstructor__ = [("([B)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getKey = JavaMethod("()[B")
    getFormat = JavaMethod("()Ljava/lang/String;")