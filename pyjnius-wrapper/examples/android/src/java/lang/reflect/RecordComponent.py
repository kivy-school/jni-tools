from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecordComponent"]

class RecordComponent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/RecordComponent"
    getName = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/Class;")
    getGenericSignature = JavaMethod("()Ljava/lang/String;")
    getGenericType = JavaMethod("()Ljava/lang/reflect/Type;")
    getAccessor = JavaMethod("()Ljava/lang/reflect/Method;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeclaringRecord = JavaMethod("()Ljava/lang/Class;")