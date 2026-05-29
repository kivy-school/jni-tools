from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXParser"]

class SAXParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/SAXParser"
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    reset = JavaMethod("()V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    parse = JavaMultipleMethod([("(Ljava/io/File;Lorg/xml/sax/HandlerBase;)V", False, False), ("(Ljava/io/File;Lorg/xml/sax/helpers/DefaultHandler;)V", False, False), ("(Lorg/xml/sax/InputSource;Lorg/xml/sax/HandlerBase;)V", False, False), ("(Lorg/xml/sax/InputSource;Lorg/xml/sax/helpers/DefaultHandler;)V", False, False), ("(Ljava/io/InputStream;Lorg/xml/sax/helpers/DefaultHandler;)V", False, False), ("(Ljava/io/InputStream;Lorg/xml/sax/HandlerBase;Ljava/lang/String;)V", False, False), ("(Ljava/io/InputStream;Lorg/xml/sax/HandlerBase;)V", False, False), ("(Ljava/lang/String;Lorg/xml/sax/helpers/DefaultHandler;)V", False, False), ("(Ljava/lang/String;Lorg/xml/sax/HandlerBase;)V", False, False), ("(Ljava/io/InputStream;Lorg/xml/sax/helpers/DefaultHandler;Ljava/lang/String;)V", False, False)])
    getXMLReader = JavaMethod("()Lorg/xml/sax/XMLReader;")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    isXIncludeAware = JavaMethod("()Z")
    getParser = JavaMethod("()Lorg/xml/sax/Parser;")