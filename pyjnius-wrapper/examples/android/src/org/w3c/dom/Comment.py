from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Comment"]

class Comment(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Comment"