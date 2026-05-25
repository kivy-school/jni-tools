from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivateKey"]

class PrivateKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivateKey"
    serialVersionUID = JavaStaticField("J")