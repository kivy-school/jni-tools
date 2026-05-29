from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Executable"]

class Executable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Executable"
    PUBLIC = JavaStaticField("I")
    DECLARED = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")
    toGenericString = JavaMethod("()Ljava/lang/String;")
    isSynthetic = JavaMethod("()Z")
    accessFlags = JavaMethod("()Ljava/util/Set;")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    isVarArgs = JavaMethod("()Z")
    getAnnotatedParameterTypes = JavaMethod("()[Ljava/lang/reflect/AnnotatedType;")
    getParameterCount = JavaMethod("()I")
    getParameterAnnotations = JavaMethod("()[[Ljava/lang/annotation/Annotation;")
    getGenericParameterTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getGenericExceptionTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getParameterTypes = JavaMethod("()[Ljava/lang/Class;")
    getExceptionTypes = JavaMethod("()[Ljava/lang/Class;")
    getAnnotatedReturnType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")
    getParameters = JavaMethod("()[Ljava/lang/reflect/Parameter;")
    getAnnotatedReceiverType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")
    getAnnotatedExceptionTypes = JavaMethod("()[Ljava/lang/reflect/AnnotatedType;")