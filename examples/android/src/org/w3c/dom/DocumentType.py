from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentType"]

class DocumentType(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DocumentType"
    getName = JavaMethod("()Ljava/lang/String;")
    getEntities = JavaMethod("()Lorg/w3c/dom/NamedNodeMap;")
    getNotations = JavaMethod("()Lorg/w3c/dom/NamedNodeMap;")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getInternalSubset = JavaMethod("()Ljava/lang/String;")