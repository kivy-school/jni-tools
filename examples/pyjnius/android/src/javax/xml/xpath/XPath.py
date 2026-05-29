from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPath"]

class XPath(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPath"
    reset = JavaMethod("()V")
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    getXPathVariableResolver = JavaMethod("()Ljavax/xml/xpath/XPathVariableResolver;")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    getXPathFunctionResolver = JavaMethod("()Ljavax/xml/xpath/XPathFunctionResolver;")
    setNamespaceContext = JavaMethod("(Ljavax/xml/namespace/NamespaceContext;)V")
    getNamespaceContext = JavaMethod("()Ljavax/xml/namespace/NamespaceContext;")
    compile = JavaMethod("(Ljava/lang/String;)Ljavax/xml/xpath/XPathExpression;")
    evaluate = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False)])