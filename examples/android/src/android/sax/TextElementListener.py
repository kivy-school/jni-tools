from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextElementListener"]

class TextElementListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/TextElementListener"