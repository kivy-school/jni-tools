from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMConfiguration"]

class DOMConfiguration(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMConfiguration"
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    canSetParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Z")
    getParameterNames = JavaMethod("()Lorg/w3c/dom/DOMStringList;")