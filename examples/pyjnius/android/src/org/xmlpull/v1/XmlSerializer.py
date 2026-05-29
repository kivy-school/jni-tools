from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlSerializer"]

class XmlSerializer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlSerializer"
    cdsect = JavaMethod("(Ljava/lang/String;)V")
    docdecl = JavaMethod("(Ljava/lang/String;)V")
    endDocument = JavaMethod("()V")
    endTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")
    entityRef = JavaMethod("(Ljava/lang/String;)V")
    ignorableWhitespace = JavaMethod("(Ljava/lang/String;)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;)V")
    setOutput = JavaMultipleMethod([("(Ljava/io/OutputStream;Ljava/lang/String;)V", False, False), ("(Ljava/io/Writer;)V", False, False)])
    setPrefix = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    startDocument = JavaMethod("(Ljava/lang/String;Ljava/lang/Boolean;)V")
    startTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")
    getName = JavaMethod("()Ljava/lang/String;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    flush = JavaMethod("()V")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    comment = JavaMethod("(Ljava/lang/String;)V")
    getDepth = JavaMethod("()I")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getPrefix = JavaMethod("(Ljava/lang/String;Z)Ljava/lang/String;")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    text = JavaMultipleMethod([("([CII)Lorg/xmlpull/v1/XmlSerializer;", False, False), ("(Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;", False, False)])
    attribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;")