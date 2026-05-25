from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamespaceContext"]

class NamespaceContext(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/namespace/NamespaceContext"
    getNamespaceURI = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrefix = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrefixes = JavaMethod("(Ljava/lang/String;)Ljava/util/Iterator;")