from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ElementListener"]

class ElementListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/ElementListener"