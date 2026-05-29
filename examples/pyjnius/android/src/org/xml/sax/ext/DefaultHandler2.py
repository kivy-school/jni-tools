from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DefaultHandler2"]

class DefaultHandler2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/DefaultHandler2"
    __javaconstructor__ = [("()V", False)]
    comment = JavaMethod("([CII)V")
    startDTD = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    endDTD = JavaMethod("()V")
    startEntity = JavaMethod("(Ljava/lang/String;)V")
    endEntity = JavaMethod("(Ljava/lang/String;)V")
    startCDATA = JavaMethod("()V")
    endCDATA = JavaMethod("()V")
    resolveEntity = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;", False, False)])
    elementDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    attributeDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    internalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    externalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getExternalSubset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")