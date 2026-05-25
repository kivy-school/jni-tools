from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ECKey"]

class ECKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECKey"
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")