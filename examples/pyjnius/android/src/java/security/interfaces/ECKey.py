from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECKey"]

class ECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECKey"
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")