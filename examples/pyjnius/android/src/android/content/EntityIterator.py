from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EntityIterator"]

class EntityIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/EntityIterator"
    reset = JavaMethod("()V")
    close = JavaMethod("()V")