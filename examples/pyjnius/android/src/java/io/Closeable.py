from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Closeable"]

class Closeable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Closeable"
    close = JavaMethod("()V")