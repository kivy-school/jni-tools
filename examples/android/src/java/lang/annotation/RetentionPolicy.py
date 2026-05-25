from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RetentionPolicy"]

class RetentionPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/RetentionPolicy"
    values = JavaStaticMethod("()[Ljava/lang/annotation/RetentionPolicy;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/annotation/RetentionPolicy;")
    SOURCE = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    CLASS = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")
    RUNTIME = JavaStaticField("Ljava/lang/annotation/RetentionPolicy;")