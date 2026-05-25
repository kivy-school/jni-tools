from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKey"]

class SecretKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKey"
    serialVersionUID = JavaStaticField("J")