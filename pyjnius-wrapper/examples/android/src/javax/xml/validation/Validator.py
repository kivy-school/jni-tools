from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Validator"]

class Validator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/Validator"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    validate = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)V", False, False), ("(Ljavax/xml/transform/Source;Ljavax/xml/transform/Result;)V", False, False)])
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")