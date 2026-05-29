from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXSource"]

class SAXSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXSource"
    __javaconstructor__ = [("(Lorg/xml/sax/InputSource;)V", False), ("(Lorg/xml/sax/XMLReader;Lorg/xml/sax/InputSource;)V", False), ("()V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getInputSource = JavaMethod("()Lorg/xml/sax/InputSource;")
    setXMLReader = JavaMethod("(Lorg/xml/sax/XMLReader;)V")
    getXMLReader = JavaMethod("()Lorg/xml/sax/XMLReader;")
    setInputSource = JavaMethod("(Lorg/xml/sax/InputSource;)V")
    sourceToInputSource = JavaStaticMethod("(Ljavax/xml/transform/Source;)Lorg/xml/sax/InputSource;")