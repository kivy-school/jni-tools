from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Key"]

class Key(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Key"
    serialVersionUID = JavaStaticField("J")
    getEncoded = JavaMethod("()[B")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")