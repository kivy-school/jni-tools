from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMImplementationList"]

class DOMImplementationList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMImplementationList"
    getLength = JavaMethod("()I")
    item = JavaMethod("(I)Lorg/w3c/dom/DOMImplementation;")