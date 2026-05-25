from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentFragment"]

class DocumentFragment(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DocumentFragment"