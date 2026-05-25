from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECKey"]

class XECKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECKey"
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")