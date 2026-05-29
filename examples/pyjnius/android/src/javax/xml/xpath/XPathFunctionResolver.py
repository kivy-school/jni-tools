from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathFunctionResolver"]

class XPathFunctionResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunctionResolver"
    resolveFunction = JavaMethod("(Ljavax/xml/namespace/QName;I)Ljavax/xml/xpath/XPathFunction;")