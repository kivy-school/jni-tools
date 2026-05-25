from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementationList"]

class DOMImplementationList(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMImplementationList"
    item = JavaMethod("(I)Lorg/w3c/dom/DOMImplementation;")
    getLength = JavaMethod("()I")