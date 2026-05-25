from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IvParameterSpec"]

class IvParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/IvParameterSpec"
    __javaconstructor__ = [("([B)V", False), ("([BII)V", False)]
    getIV = JavaMethod("()[B")