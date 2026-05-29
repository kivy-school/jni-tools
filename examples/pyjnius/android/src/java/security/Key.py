from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Key"]

class Key(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Key"
    serialVersionUID = JavaStaticField("J")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")