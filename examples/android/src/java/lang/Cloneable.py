from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cloneable"]

class Cloneable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Cloneable"