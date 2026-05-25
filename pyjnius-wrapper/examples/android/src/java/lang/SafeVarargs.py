from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SafeVarargs"]

class SafeVarargs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/SafeVarargs"