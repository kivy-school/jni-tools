from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class XPathFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunction"
    evaluate = JavaMethod("(Ljava/util/List;)Ljava/lang/Object;")

class XPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPath"
    evaluate = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False)])
    evaluateExpression = JavaMultipleMethod([("(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljava/lang/Class;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;", False, False)])
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    getXPathVariableResolver = JavaMethod("()Ljavax/xml/xpath/XPathVariableResolver;")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    getXPathFunctionResolver = JavaMethod("()Ljavax/xml/xpath/XPathFunctionResolver;")
    setNamespaceContext = JavaMethod("(Ljavax/xml/namespace/NamespaceContext;)V")
    getNamespaceContext = JavaMethod("()Ljavax/xml/namespace/NamespaceContext;")
    reset = JavaMethod("()V")
    compile = JavaMethod("(Ljava/lang/String;)Ljavax/xml/xpath/XPathExpression;")

class XPathFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFactory"
    DEFAULT_PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    DEFAULT_OBJECT_MODEL_URI = JavaStaticField("Ljava/lang/String;")
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    isObjectModelSupported = JavaMethod("(Ljava/lang/String;)Z")
    newXPath = JavaMethod("()Ljavax/xml/xpath/XPath;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/xpath/XPathFactory;", True, False), ("(Ljava/lang/String;)Ljavax/xml/xpath/XPathFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/xpath/XPathFactory;", True, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/xpath/XPathFactory;")

class XPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]
    printStackTrace = JavaMultipleMethod([("(Ljava/io/PrintWriter;)V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("()V", False, False)])
    getCause = JavaMethod("()Ljava/lang/Throwable;")

class XPathFunctionResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunctionResolver"
    resolveFunction = JavaMethod("(Ljavax/xml/namespace/QName;I)Ljavax/xml/xpath/XPathFunction;")

class XPathExpressionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathExpressionException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class XPathVariableResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathVariableResolver"
    resolveVariable = JavaMethod("(Ljavax/xml/namespace/QName;)Ljava/lang/Object;")

class XPathFactoryConfigurationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFactoryConfigurationException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class XPathFunctionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunctionException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class XPathExpression(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathExpression"
    evaluate = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False), ("(Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False)])
    evaluateExpression = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;Ljava/lang/Class;)Ljava/lang/Object;", False, False), ("(Lorg/xml/sax/InputSource;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/Object;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;", False, False)])

class XPathConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathConstants"
    NUMBER = JavaStaticField("Ljavax/xml/namespace/QName;")
    STRING = JavaStaticField("Ljavax/xml/namespace/QName;")
    BOOLEAN = JavaStaticField("Ljavax/xml/namespace/QName;")
    NODESET = JavaStaticField("Ljavax/xml/namespace/QName;")
    NODE = JavaStaticField("Ljavax/xml/namespace/QName;")
    DOM_OBJECT_MODEL = JavaStaticField("Ljava/lang/String;")