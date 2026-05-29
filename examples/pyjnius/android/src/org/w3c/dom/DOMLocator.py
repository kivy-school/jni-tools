from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMLocator"]

class DOMLocator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMLocator"
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")
    getByteOffset = JavaMethod("()I")
    getUtf16Offset = JavaMethod("()I")
    getRelatedNode = JavaMethod("()Lorg/w3c/dom/Node;")
    getUri = JavaMethod("()Ljava/lang/String;")