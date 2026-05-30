from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SAXResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXResult"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/ContentHandler;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    setLexicalHandler = JavaMethod("(Lorg/xml/sax/ext/LexicalHandler;)V")
    getLexicalHandler = JavaMethod("()Lorg/xml/sax/ext/LexicalHandler;")
    getHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")

class SAXTransformerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXTransformerFactory"
    FEATURE = JavaStaticField("Ljava/lang/String;")
    FEATURE_XMLFILTER = JavaStaticField("Ljava/lang/String;")
    newTransformerHandler = JavaMultipleMethod([("(Ljavax/xml/transform/Templates;)Ljavax/xml/transform/sax/TransformerHandler;", False, False), ("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/sax/TransformerHandler;", False, False), ("()Ljavax/xml/transform/sax/TransformerHandler;", False, False)])
    newTemplatesHandler = JavaMethod("()Ljavax/xml/transform/sax/TemplatesHandler;")
    newXMLFilter = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)Lorg/xml/sax/XMLFilter;", False, False), ("(Ljavax/xml/transform/Templates;)Lorg/xml/sax/XMLFilter;", False, False)])

class TransformerHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TransformerHandler"
    setResult = JavaMethod("(Ljavax/xml/transform/Result;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")

class TemplatesHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/TemplatesHandler"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getTemplates = JavaMethod("()Ljavax/xml/transform/Templates;")

class SAXSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXSource"
    __javaconstructor__ = [("(Lorg/xml/sax/XMLReader;Lorg/xml/sax/InputSource;)V", False), ("(Lorg/xml/sax/InputSource;)V", False), ("()V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getInputSource = JavaMethod("()Lorg/xml/sax/InputSource;")
    setXMLReader = JavaMethod("(Lorg/xml/sax/XMLReader;)V")
    getXMLReader = JavaMethod("()Lorg/xml/sax/XMLReader;")
    setInputSource = JavaMethod("(Lorg/xml/sax/InputSource;)V")
    sourceToInputSource = JavaStaticMethod("(Ljavax/xml/transform/Source;)Lorg/xml/sax/InputSource;")
    isEmpty = JavaMethod("()Z")