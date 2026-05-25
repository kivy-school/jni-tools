from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Native"]

class Native(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Native"