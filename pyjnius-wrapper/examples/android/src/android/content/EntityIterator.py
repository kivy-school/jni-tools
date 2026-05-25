from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EntityIterator"]

class EntityIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/EntityIterator"
    reset = JavaMethod("()V")
    close = JavaMethod("()V")