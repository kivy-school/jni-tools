from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutoCloseable"]

class AutoCloseable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/AutoCloseable"
    close = JavaMethod("()V")