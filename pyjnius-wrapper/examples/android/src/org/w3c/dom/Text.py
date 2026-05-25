from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Text"]

class Text(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Text"
    splitText = JavaMethod("(I)Lorg/w3c/dom/Text;")
    isElementContentWhitespace = JavaMethod("()Z")
    getWholeText = JavaMethod("()Ljava/lang/String;")
    replaceWholeText = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Text;")