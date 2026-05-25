from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrappedKeyEntry"]

class WrappedKeyEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/WrappedKeyEntry"
    __javaconstructor__ = [("([BLjava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getWrappedKeyBytes = JavaMethod("()[B")
    getWrappingKeyAlias = JavaMethod("()Ljava/lang/String;")
    getTransformation = JavaMethod("()Ljava/lang/String;")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")