from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SourceLocator"]

class SourceLocator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/SourceLocator"
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")