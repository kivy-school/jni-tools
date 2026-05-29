from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaFactory"]

class SchemaFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactory"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/validation/SchemaFactory;", True, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    isSchemaLanguageSupported = JavaMethod("(Ljava/lang/String;)Z")
    newSchema = JavaMultipleMethod([("(Ljava/io/File;)Ljavax/xml/validation/Schema;", False, False), ("(Ljava/net/URL;)Ljavax/xml/validation/Schema;", False, False), ("([Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("(Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("()Ljavax/xml/validation/Schema;", False, False)])
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/validation/SchemaFactory;")