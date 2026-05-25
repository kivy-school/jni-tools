from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Locator2"]

class Locator2(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Locator2"
    getXMLVersion = JavaMethod("()Ljava/lang/String;")
    getEncoding = JavaMethod("()Ljava/lang/String;")