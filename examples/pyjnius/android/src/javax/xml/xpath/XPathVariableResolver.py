from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathVariableResolver"]

class XPathVariableResolver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathVariableResolver"
    resolveVariable = JavaMethod("(Ljavax/xml/namespace/QName;)Ljava/lang/Object;")