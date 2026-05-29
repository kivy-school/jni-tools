from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathFunction"]

class XPathFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathFunction"
    evaluate = JavaMethod("(Ljava/util/List;)Ljava/lang/Object;")