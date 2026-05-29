from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Flushable"]

class Flushable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Flushable"
    flush = JavaMethod("()V")