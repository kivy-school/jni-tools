from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParameterSpec"]

class AlgorithmParameterSpec(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/AlgorithmParameterSpec"