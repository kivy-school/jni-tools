from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Notation"]

class Notation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Notation"
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")