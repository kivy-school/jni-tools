from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextElementListener"]

class TextElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/TextElementListener"