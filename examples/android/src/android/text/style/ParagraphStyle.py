from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParagraphStyle"]

class ParagraphStyle(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ParagraphStyle"