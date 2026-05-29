from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMLocator"]

class DOMLocator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMLocator"
    getOriginatingNode = JavaMethod("()Lorg/w3c/dom/Node;")