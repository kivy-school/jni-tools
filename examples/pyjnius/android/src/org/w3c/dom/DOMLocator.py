from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMLocator"]

class DOMLocator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMLocator"
    getUri = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getByteOffset = JavaMethod("()I")
    getUtf16Offset = JavaMethod("()I")
    getRelatedNode = JavaMethod("()Lorg/w3c/dom/Node;")
    getLineNumber = JavaMethod("()I")