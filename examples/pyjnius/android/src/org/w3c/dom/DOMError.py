from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMError"]

class DOMError(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMError"
    SEVERITY_ERROR = JavaStaticField("S")
    SEVERITY_FATAL_ERROR = JavaStaticField("S")
    SEVERITY_WARNING = JavaStaticField("S")
    getSeverity = JavaMethod("()S")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getRelatedException = JavaMethod("()Ljava/lang/Object;")
    getRelatedData = JavaMethod("()Ljava/lang/Object;")
    getLocation = JavaMethod("()Lorg/w3c/dom/DOMLocator;")