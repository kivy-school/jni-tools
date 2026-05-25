from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathFactory"]

class XPathFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFactory"
    __javaconstructor__ = [("()V", False)]
    DEFAULT_OBJECT_MODEL_URI = JavaStaticField("Ljava/lang/String;")
    DEFAULT_PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/xpath/XPathFactory;", True, False), ("(Ljava/lang/String;)Ljavax/xml/xpath/XPathFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/xpath/XPathFactory;", True, False)])
    isObjectModelSupported = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    newXPath = JavaMethod("()Ljavax/xml/xpath/XPath;")