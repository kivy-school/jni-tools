from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Entity"]

class Entity(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Entity"
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getNotationName = JavaMethod("()Ljava/lang/String;")
    getInputEncoding = JavaMethod("()Ljava/lang/String;")
    getXmlEncoding = JavaMethod("()Ljava/lang/String;")
    getXmlVersion = JavaMethod("()Ljava/lang/String;")