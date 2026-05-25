from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXResult"]

class SAXResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXResult"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/ContentHandler;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    setLexicalHandler = JavaMethod("(Lorg/xml/sax/ext/LexicalHandler;)V")
    getLexicalHandler = JavaMethod("()Lorg/xml/sax/ext/LexicalHandler;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")