from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSResourceResolver"]

class LSResourceResolver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSResourceResolver"
    resolveResource = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/ls/LSInput;")