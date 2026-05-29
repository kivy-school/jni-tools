from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XPathConstants"]

class XPathConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/xpath/XPathConstants"
    NUMBER = JavaStaticField("Ljavax/xml/namespace/QName;")
    STRING = JavaStaticField("Ljavax/xml/namespace/QName;")
    BOOLEAN = JavaStaticField("Ljavax/xml/namespace/QName;")
    NODESET = JavaStaticField("Ljavax/xml/namespace/QName;")
    NODE = JavaStaticField("Ljavax/xml/namespace/QName;")
    DOM_OBJECT_MODEL = JavaStaticField("Ljava/lang/String;")