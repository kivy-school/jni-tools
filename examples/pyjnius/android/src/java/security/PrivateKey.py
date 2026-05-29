from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivateKey"]

class PrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")