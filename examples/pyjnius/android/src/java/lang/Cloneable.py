from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cloneable"]

class Cloneable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Cloneable"