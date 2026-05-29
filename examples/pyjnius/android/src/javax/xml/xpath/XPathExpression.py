from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathExpression"]

class XPathExpression(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathExpression"
    evaluate = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False), ("(Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False)])
    evaluateExpression = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;Ljava/lang/Class;)Ljava/lang/Object;", False, False), ("(Lorg/xml/sax/InputSource;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/Object;)Ljavax/xml/xpath/XPathEvaluationResult;", False, False), ("(Ljava/lang/Object;Ljava/lang/Class;)Ljava/lang/Object;", False, False)])