from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IvParameterSpec"]

class IvParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/IvParameterSpec"
    __javaconstructor__ = [("([BII)V", False), ("([B)V", False)]
    getIV = JavaMethod("()[B")