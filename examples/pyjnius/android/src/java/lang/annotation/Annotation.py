from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Annotation"]

class Annotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/Annotation"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    annotationType = JavaMethod("()Ljava/lang/Class;")