from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Locator2"]

class Locator2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Locator2"
    getEncoding = JavaMethod("()Ljava/lang/String;")
    getXMLVersion = JavaMethod("()Ljava/lang/String;")