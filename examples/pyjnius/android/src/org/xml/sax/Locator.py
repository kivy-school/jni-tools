from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Locator"]

class Locator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Locator"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")