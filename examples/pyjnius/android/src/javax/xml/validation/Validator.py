from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validator"]

class Validator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/Validator"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    reset = JavaMethod("()V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    validate = JavaMultipleMethod([("(Ljavax/xml/transform/Source;Ljavax/xml/transform/Result;)V", False, False), ("(Ljavax/xml/transform/Source;)V", False, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")