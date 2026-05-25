from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValidatorHandler"]

class ValidatorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/ValidatorHandler"
    __javaconstructor__ = [("()V", False)]
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    getTypeInfoProvider = JavaMethod("()Ljavax/xml/validation/TypeInfoProvider;")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")