from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Annotation"]

class Annotation(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Annotation"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    annotationType = JavaMethod("()Ljava/lang/Class;")