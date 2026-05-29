from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PSource"]

class PSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PSource"
    getAlgorithm = JavaMethod("()Ljava/lang/String;")

    class PSpecified(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/crypto/spec/PSource$PSpecified"
        __javaconstructor__ = [("([B)V", False)]
        DEFAULT = JavaStaticField("Ljavax/crypto/spec/PSource$PSpecified;")
        getValue = JavaMethod("()[B")