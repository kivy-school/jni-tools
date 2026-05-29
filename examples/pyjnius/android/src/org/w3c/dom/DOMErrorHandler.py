from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMErrorHandler"]

class DOMErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMErrorHandler"
    handleError = JavaMethod("(Lorg/w3c/dom/DOMError;)Z")