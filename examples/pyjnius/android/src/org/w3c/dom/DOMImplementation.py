from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementation"]

class DOMImplementation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMImplementation"
    createDocument = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lorg/w3c/dom/DocumentType;)Lorg/w3c/dom/Document;")
    getFeature = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")
    hasFeature = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    createDocumentType = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/DocumentType;")