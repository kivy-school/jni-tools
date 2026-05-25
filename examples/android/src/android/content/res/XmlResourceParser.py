from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlResourceParser"]

class XmlResourceParser(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/XmlResourceParser"
    getAttributeNamespace = JavaMethod("(I)Ljava/lang/String;")
    close = JavaMethod("()V")