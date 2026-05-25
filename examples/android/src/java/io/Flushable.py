from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Flushable"]

class Flushable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Flushable"
    flush = JavaMethod("()V")