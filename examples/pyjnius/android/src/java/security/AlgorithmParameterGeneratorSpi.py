from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameterGeneratorSpi"]

class AlgorithmParameterGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParameterGeneratorSpi"
    __javaconstructor__ = [("()V", False)]