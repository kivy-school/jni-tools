from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlSerializer"]

class XmlSerializer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlSerializer"
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setOutput = JavaMultipleMethod([("(Ljava/io/OutputStream;Ljava/lang/String;)V", False, False), ("(Ljava/io/Writer;)V", False, False)])
    startDocument = JavaMethod("(Ljava/lang/String;Ljava/lang/Boolean;)V")
    endDocument = JavaMethod("()V")
    setPrefix = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getPrefix = JavaMethod("(Ljava/lang/String;Z)Ljava/lang/String;")
    getDepth = JavaMethod("()I")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    startTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")
    attribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")
    endTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")
    text = JavaMultipleMethod([("(Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;", False, False), ("([CII)Lorg/xmlpull/v1/XmlSerializer;", False, False)])
    cdsect = JavaMethod("(Ljava/lang/String;)V")
    entityRef = JavaMethod("(Ljava/lang/String;)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;)V")
    comment = JavaMethod("(Ljava/lang/String;)V")
    docdecl = JavaMethod("(Ljava/lang/String;)V")
    ignorableWhitespace = JavaMethod("(Ljava/lang/String;)V")
    flush = JavaMethod("()V")