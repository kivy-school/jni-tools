from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamespaceContext"]

class NamespaceContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/namespace/NamespaceContext"
    getPrefix = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getNamespaceURI = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrefixes = JavaMethod("(Ljava/lang/String;)Ljava/util/Iterator;")