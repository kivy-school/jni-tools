from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaFactory"]

class SchemaFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactory"
    __javaconstructor__ = [("()V", False)]
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/validation/SchemaFactory;", True, False)])
    isSchemaLanguageSupported = JavaMethod("(Ljava/lang/String;)Z")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    newSchema = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("(Ljava/io/File;)Ljavax/xml/validation/Schema;", False, False), ("(Ljava/net/URL;)Ljavax/xml/validation/Schema;", False, False), ("([Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("()Ljavax/xml/validation/Schema;", False, False)])