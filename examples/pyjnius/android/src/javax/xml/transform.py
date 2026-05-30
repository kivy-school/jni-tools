from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Transformer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Transformer"
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setURIResolver = JavaMethod("(Ljavax/xml/transform/URIResolver;)V")
    getURIResolver = JavaMethod("()Ljavax/xml/transform/URIResolver;")
    setOutputProperties = JavaMethod("(Ljava/util/Properties;)V")
    getOutputProperties = JavaMethod("()Ljava/util/Properties;")
    setOutputProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getOutputProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setErrorListener = JavaMethod("(Ljavax/xml/transform/ErrorListener;)V")
    getErrorListener = JavaMethod("()Ljavax/xml/transform/ErrorListener;")
    reset = JavaMethod("()V")
    transform = JavaMethod("(Ljavax/xml/transform/Source;Ljavax/xml/transform/Result;)V")
    clearParameters = JavaMethod("()V")

class OutputKeys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/OutputKeys"
    METHOD = JavaStaticField("Ljava/lang/String;")
    VERSION = JavaStaticField("Ljava/lang/String;")
    ENCODING = JavaStaticField("Ljava/lang/String;")
    OMIT_XML_DECLARATION = JavaStaticField("Ljava/lang/String;")
    STANDALONE = JavaStaticField("Ljava/lang/String;")
    DOCTYPE_PUBLIC = JavaStaticField("Ljava/lang/String;")
    DOCTYPE_SYSTEM = JavaStaticField("Ljava/lang/String;")
    CDATA_SECTION_ELEMENTS = JavaStaticField("Ljava/lang/String;")
    INDENT = JavaStaticField("Ljava/lang/String;")
    MEDIA_TYPE = JavaStaticField("Ljava/lang/String;")

class TransformerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;)V", False)]
    getLocationAsString = JavaMethod("()Ljava/lang/String;")
    getLocator = JavaMethod("()Ljavax/xml/transform/SourceLocator;")
    setLocator = JavaMethod("(Ljavax/xml/transform/SourceLocator;)V")
    getMessageAndLocation = JavaMethod("()Ljava/lang/String;")
    printStackTrace = JavaMultipleMethod([("(Ljava/io/PrintWriter;)V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("()V", False, False)])
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    getException = JavaMethod("()Ljava/lang/Throwable;")

class SourceLocator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/SourceLocator"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getLineNumber = JavaMethod("()I")

class Templates(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Templates"
    getOutputProperties = JavaMethod("()Ljava/util/Properties;")
    newTransformer = JavaMethod("()Ljavax/xml/transform/Transformer;")

class TransformerFactoryConfigurationError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactoryConfigurationError"
    __javaconstructor__ = [("(Ljava/lang/Exception;Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")

class TransformerConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerConfigurationException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljavax/xml/transform/SourceLocator;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class Source(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Source"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    isEmpty = JavaMethod("()Z")

class Result(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/Result"
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")

class URIResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/URIResolver"
    resolve = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")

class TransformerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/TransformerFactory"
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setURIResolver = JavaMethod("(Ljavax/xml/transform/URIResolver;)V")
    getURIResolver = JavaMethod("()Ljavax/xml/transform/URIResolver;")
    setErrorListener = JavaMethod("(Ljavax/xml/transform/ErrorListener;)V")
    getErrorListener = JavaMethod("()Ljavax/xml/transform/ErrorListener;")
    newTransformer = JavaMultipleMethod([("()Ljavax/xml/transform/Transformer;", False, False), ("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Transformer;", False, False)])
    newTemplates = JavaMethod("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/Templates;")
    getAssociatedStylesheet = JavaMethod("(Ljavax/xml/transform/Source;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljavax/xml/transform/Source;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/transform/TransformerFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/transform/TransformerFactory;", True, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/transform/TransformerFactory;")

class ErrorListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/ErrorListener"
    warning = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")
    error = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")
    fatalError = JavaMethod("(Ljavax/xml/transform/TransformerException;)V")