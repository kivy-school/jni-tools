from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Retention"]

class Retention(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Retention"
    value = JavaMethod("()Ljava/lang/annotation/RetentionPolicy;")