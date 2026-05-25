from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublicKey"]

class PublicKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PublicKey"
    serialVersionUID = JavaStaticField("J")