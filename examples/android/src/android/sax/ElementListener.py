from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ElementListener"]

class ElementListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/ElementListener"