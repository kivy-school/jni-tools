from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parameter"]

class Parameter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Parameter"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    isNamePresent = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeclaringExecutable = JavaMethod("()Ljava/lang/reflect/Executable;")
    getModifiers = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getParameterizedType = JavaMethod("()Ljava/lang/reflect/Type;")
    getType = JavaMethod("()Ljava/lang/Class;")
    isImplicit = JavaMethod("()Z")
    isSynthetic = JavaMethod("()Z")
    isVarArgs = JavaMethod("()Z")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")