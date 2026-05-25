from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathExpression"]

class XPathExpression(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathExpression"
    evaluate = JavaMultipleMethod([("(Ljava/lang/Object;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Ljava/lang/String;", False, False), ("(Lorg/xml/sax/InputSource;Ljavax/xml/namespace/QName;)Ljava/lang/Object;", False, False), ("(Lorg/xml/sax/InputSource;)Ljava/lang/String;", False, False)])