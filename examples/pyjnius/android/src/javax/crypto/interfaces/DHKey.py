from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DHKey"]

class DHKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/interfaces/DHKey"
    getParams = JavaMethod("()Ljavax/crypto/spec/DHParameterSpec;")