from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NClob"]

class NClob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/NClob"