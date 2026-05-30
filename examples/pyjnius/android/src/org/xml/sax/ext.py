from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Locator2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Locator2"
    getXMLVersion = JavaMethod("()Ljava/lang/String;")
    getEncoding = JavaMethod("()Ljava/lang/String;")

class LexicalHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/LexicalHandler"
    startDTD = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    endDTD = JavaMethod("()V")
    startEntity = JavaMethod("(Ljava/lang/String;)V")
    endEntity = JavaMethod("(Ljava/lang/String;)V")
    startCDATA = JavaMethod("()V")
    endCDATA = JavaMethod("()V")
    comment = JavaMethod("([CII)V")

class Attributes2Impl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2Impl"
    __javaconstructor__ = [("(Lorg/xml/sax/Attributes;)V", False), ("()V", False)]
    setAttributes = JavaMethod("(Lorg/xml/sax/Attributes;)V")
    removeAttribute = JavaMethod("(I)V")
    isDeclared = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])
    setDeclared = JavaMethod("(IZ)V")
    setSpecified = JavaMethod("(IZ)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    isSpecified = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(I)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])

class DeclHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/DeclHandler"
    elementDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    attributeDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    internalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    externalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")

class EntityResolver2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/EntityResolver2"
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    getExternalSubset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")

class DefaultHandler2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/DefaultHandler2"
    __javaconstructor__ = [("()V", False)]
    resolveEntity = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;", False, False)])
    startDTD = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    endDTD = JavaMethod("()V")
    startEntity = JavaMethod("(Ljava/lang/String;)V")
    endEntity = JavaMethod("(Ljava/lang/String;)V")
    startCDATA = JavaMethod("()V")
    endCDATA = JavaMethod("()V")
    elementDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    attributeDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    internalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    externalEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getExternalSubset = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    comment = JavaMethod("([CII)V")

class Locator2Impl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Locator2Impl"
    __javaconstructor__ = [("(Lorg/xml/sax/Locator;)V", False), ("()V", False)]
    getXMLVersion = JavaMethod("()Ljava/lang/String;")
    setXMLVersion = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")

class Attributes2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2"
    isDeclared = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])
    isSpecified = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])