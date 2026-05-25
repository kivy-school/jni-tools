from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Target"]

class Target(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Target"
    value = JavaMethod("()[Ljava/lang/annotation/ElementType;")