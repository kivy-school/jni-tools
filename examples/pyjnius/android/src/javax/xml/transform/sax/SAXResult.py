from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXResult"]

class SAXResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXResult"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/ContentHandler;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    setHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    setLexicalHandler = JavaMethod("(Lorg/xml/sax/ext/LexicalHandler;)V")
    getLexicalHandler = JavaMethod("()Lorg/xml/sax/ext/LexicalHandler;")