from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Repeatable"]

class Repeatable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Repeatable"
    value = JavaMethod("()Ljava/lang/Class;")