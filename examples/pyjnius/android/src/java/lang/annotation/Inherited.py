from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inherited"]

class Inherited(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Inherited"