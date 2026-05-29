from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XECKey"]

class XECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECKey"
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")