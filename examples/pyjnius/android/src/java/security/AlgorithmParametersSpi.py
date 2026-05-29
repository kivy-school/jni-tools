from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlgorithmParametersSpi"]

class AlgorithmParametersSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AlgorithmParametersSpi"
    __javaconstructor__ = [("()V", False)]