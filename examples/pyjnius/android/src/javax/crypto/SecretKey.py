from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecretKey"]

class SecretKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")