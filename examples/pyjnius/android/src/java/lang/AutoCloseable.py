from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutoCloseable"]

class AutoCloseable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/AutoCloseable"
    close = JavaMethod("()V")