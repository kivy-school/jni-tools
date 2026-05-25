from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Documented"]

class Documented(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Documented"