from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SourceLocator"]

class SourceLocator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/SourceLocator"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")