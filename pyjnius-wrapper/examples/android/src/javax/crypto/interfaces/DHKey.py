from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHKey"]

class DHKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHKey"
    getParams = JavaMethod("()Ljavax/crypto/spec/DHParameterSpec;")