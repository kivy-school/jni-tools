from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPath"]

class XPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPath"
    reset = JavaMethod("()V")
    compile = JavaMethod("(Ljava/lang/String;)Ljavax/xml/xpath/XPathExpression;")
    evaluate = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False)])
    evaluateExpression = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Ljava/lang/Object;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;Ljava/lang/Class;)Ljava/lang/Object;", False, False), ("(Ljava/lang/String;Lorg/xml/sax/InputSource;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False)])
    setXPathVariableResolver = JavaMethod("(Ljavax/xml/xpath/XPathVariableResolver;)V")
    getXPathVariableResolver = JavaMethod("()Ljavax/xml/xpath/XPathVariableResolver;")
    setXPathFunctionResolver = JavaMethod("(Ljavax/xml/xpath/XPathFunctionResolver;)V")
    getXPathFunctionResolver = JavaMethod("()Ljavax/xml/xpath/XPathFunctionResolver;")
    setNamespaceContext = JavaMethod("(Ljavax/xml/namespace/NamespaceContext;)V")
    getNamespaceContext = JavaMethod("()Ljavax/xml/namespace/NamespaceContext;")