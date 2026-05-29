from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementationSource"]

class DOMImplementationSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMImplementationSource"
    getDOMImplementation = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/DOMImplementation;")
    getDOMImplementationList = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/DOMImplementationList;")