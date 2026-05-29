from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathFunctionResolver"]

class XPathFunctionResolver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunctionResolver"
    resolveFunction = JavaMethod("(Ljavax/xml/namespace/QName;I)Ljavax/xml/xpath/XPathFunction;")