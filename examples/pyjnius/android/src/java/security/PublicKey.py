from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublicKey"]

class PublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")