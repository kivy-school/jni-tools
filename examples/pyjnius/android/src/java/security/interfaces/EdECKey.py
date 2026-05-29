from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdECKey"]

class EdECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECKey"
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")