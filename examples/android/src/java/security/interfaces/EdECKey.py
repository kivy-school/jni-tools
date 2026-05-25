from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECKey"]

class EdECKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECKey"
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")