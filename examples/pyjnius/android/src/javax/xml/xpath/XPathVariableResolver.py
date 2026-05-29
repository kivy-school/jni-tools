from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathVariableResolver"]

class XPathVariableResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathVariableResolver"
    resolveVariable = JavaMethod("(Ljavax/xml/namespace/QName;)Ljava/lang/Object;")