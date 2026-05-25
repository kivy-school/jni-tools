from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Locator"]

class Locator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Locator"
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")