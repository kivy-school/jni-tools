from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Serial"]

class Serial(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Serial"