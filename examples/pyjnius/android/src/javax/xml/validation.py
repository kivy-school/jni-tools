from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Validator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/Validator"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    reset = JavaMethod("()V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    validate = JavaMultipleMethod([("(Ljavax/xml/transform/Source;)V", False, False), ("(Ljavax/xml/transform/Source;Ljavax/xml/transform/Result;)V", False, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")

class ValidatorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/ValidatorHandler"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    getTypeInfoProvider = JavaMethod("()Ljavax/xml/validation/TypeInfoProvider;")

class SchemaFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactory"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/validation/SchemaFactory;", True, False), ("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;", True, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setResourceResolver = JavaMethod("(Lorg/w3c/dom/ls/LSResourceResolver;)V")
    getResourceResolver = JavaMethod("()Lorg/w3c/dom/ls/LSResourceResolver;")
    isSchemaLanguageSupported = JavaMethod("(Ljava/lang/String;)Z")
    newSchema = JavaMultipleMethod([("()Ljavax/xml/validation/Schema;", False, False), ("(Ljava/net/URL;)Ljavax/xml/validation/Schema;", False, False), ("([Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("(Ljavax/xml/transform/Source;)Ljavax/xml/validation/Schema;", False, False), ("(Ljava/io/File;)Ljavax/xml/validation/Schema;", False, False)])
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/validation/SchemaFactory;")

class TypeInfoProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/TypeInfoProvider"
    getElementTypeInfo = JavaMethod("()Lorg/w3c/dom/TypeInfo;")
    getAttributeTypeInfo = JavaMethod("(I)Lorg/w3c/dom/TypeInfo;")
    isIdAttribute = JavaMethod("(I)Z")
    isSpecified = JavaMethod("(I)Z")

class SchemaFactoryLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/SchemaFactoryLoader"
    newFactory = JavaMethod("(Ljava/lang/String;)Ljavax/xml/validation/SchemaFactory;")

class Schema(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/validation/Schema"
    newValidator = JavaMethod("()Ljavax/xml/validation/Validator;")
    newValidatorHandler = JavaMethod("()Ljavax/xml/validation/ValidatorHandler;")