from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementation"]

class DOMImplementation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMImplementation"
    hasFeature = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    createDocumentType = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/DocumentType;")
    createDocument = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lorg/w3c/dom/DocumentType;)Lorg/w3c/dom/Document;")
    getFeature = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")