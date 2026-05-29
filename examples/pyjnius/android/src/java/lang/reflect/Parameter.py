from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parameter"]

class Parameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Parameter"
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getModifiers = JavaMethod("()I")
    isSynthetic = JavaMethod("()Z")
    accessFlags = JavaMethod("()Ljava/util/Set;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getType = JavaMethod("()Ljava/lang/Class;")
    getAnnotatedType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")
    getParameterizedType = JavaMethod("()Ljava/lang/reflect/Type;")
    isVarArgs = JavaMethod("()Z")
    getDeclaringExecutable = JavaMethod("()Ljava/lang/reflect/Executable;")
    isNamePresent = JavaMethod("()Z")
    isImplicit = JavaMethod("()Z")