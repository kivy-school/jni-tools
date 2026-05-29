from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECPoint"]

class EdECPoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPoint"
    __javaconstructor__ = [("(ZLjava/math/BigInteger;)V", False)]
    isXOdd = JavaMethod("()Z")
    getY = JavaMethod("()Ljava/math/BigInteger;")