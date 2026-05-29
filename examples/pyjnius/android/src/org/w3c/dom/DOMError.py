from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMError"]

class DOMError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMError"
    SEVERITY_WARNING = JavaStaticField("S")
    SEVERITY_ERROR = JavaStaticField("S")
    SEVERITY_FATAL_ERROR = JavaStaticField("S")
    getLocation = JavaMethod("()Lorg/w3c/dom/DOMLocator;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getRelatedException = JavaMethod("()Ljava/lang/Object;")
    getRelatedData = JavaMethod("()Ljava/lang/Object;")
    getSeverity = JavaMethod("()S")