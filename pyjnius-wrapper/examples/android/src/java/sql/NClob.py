from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NClob"]

class NClob(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/NClob"