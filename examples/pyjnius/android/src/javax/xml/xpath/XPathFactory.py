from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathFactory"]

class XPathFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFactory"
    DEFAULT_PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    DEFAULT_OBJECT_MODEL_URI = JavaStaticField("Ljava/lang/String;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/xpath/XPathFactory;", True, False), ("(Ljava/lang/String;)Ljavax/xml/xpath/XPathFactory;", True, False), ("()Ljavax/xml/xpath/XPathFactory;", True, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/xpath/XPathFactory;")
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    isObjectModelSupported = JavaMethod("(Ljava/lang/String;)Z")
    newXPath = JavaMethod("()Ljavax/xml/xpath/XPath;")