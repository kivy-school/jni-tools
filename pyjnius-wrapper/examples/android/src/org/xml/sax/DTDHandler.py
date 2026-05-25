from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DTDHandler"]

class DTDHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/DTDHandler"
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")