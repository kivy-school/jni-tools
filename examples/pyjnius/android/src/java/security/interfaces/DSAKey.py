from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAKey"]

class DSAKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKey"
    getParams = JavaMethod("()Ljava/security/interfaces/DSAParams;")