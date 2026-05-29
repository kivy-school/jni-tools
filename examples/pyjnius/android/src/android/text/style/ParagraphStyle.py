from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParagraphStyle"]

class ParagraphStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ParagraphStyle"