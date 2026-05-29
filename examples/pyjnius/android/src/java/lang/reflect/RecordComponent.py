from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecordComponent"]

class RecordComponent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/RecordComponent"
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getGenericSignature = JavaMethod("()Ljava/lang/String;")
    getGenericType = JavaMethod("()Ljava/lang/reflect/Type;")
    getType = JavaMethod("()Ljava/lang/Class;")
    getAnnotatedType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")
    getAccessor = JavaMethod("()Ljava/lang/reflect/Method;")
    getDeclaringRecord = JavaMethod("()Ljava/lang/Class;")