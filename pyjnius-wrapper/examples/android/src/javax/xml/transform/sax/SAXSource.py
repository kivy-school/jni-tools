from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXSource"]

class SAXSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXSource"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/XMLReader;Lorg/xml/sax/InputSource;)V", False), ("(Lorg/xml/sax/InputSource;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setXMLReader = JavaMethod("(Lorg/xml/sax/XMLReader;)V")
    getXMLReader = JavaMethod("()Lorg/xml/sax/XMLReader;")
    setInputSource = JavaMethod("(Lorg/xml/sax/InputSource;)V")
    getInputSource = JavaMethod("()Lorg/xml/sax/InputSource;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    sourceToInputSource = JavaStaticMethod("(Ljavax/xml/transform/Source;)Lorg/xml/sax/InputSource;")