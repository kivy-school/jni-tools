from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SuppressWarnings"]

class SuppressWarnings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/SuppressWarnings"
    value = JavaMethod("()[Ljava/lang/String;")