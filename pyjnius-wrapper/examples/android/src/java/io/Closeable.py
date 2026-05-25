from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Closeable"]

class Closeable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Closeable"
    close = JavaMethod("()V")