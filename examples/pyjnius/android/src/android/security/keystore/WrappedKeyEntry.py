from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrappedKeyEntry"]

class WrappedKeyEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/WrappedKeyEntry"
    __javaconstructor__ = [("([BLjava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getWrappingKeyAlias = JavaMethod("()Ljava/lang/String;")
    getWrappedKeyBytes = JavaMethod("()[B")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getTransformation = JavaMethod("()Ljava/lang/String;")