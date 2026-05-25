from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMLocator"]

class DOMLocator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMLocator"
    getOriginatingNode = JavaMethod("()Lorg/w3c/dom/Node;")