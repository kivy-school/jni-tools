from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DSAKey"]

class DSAKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKey"
    getParams = JavaMethod("()Ljava/security/interfaces/DSAParams;")