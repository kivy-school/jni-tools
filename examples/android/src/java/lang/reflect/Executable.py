from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Executable"]

class Executable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Executable"
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    getName = JavaMethod("()Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")
    getParameterTypes = JavaMethod("()[Ljava/lang/Class;")
    getParameterCount = JavaMethod("()I")
    getGenericParameterTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getParameters = JavaMethod("()[Ljava/lang/reflect/Parameter;")
    getExceptionTypes = JavaMethod("()[Ljava/lang/Class;")
    getGenericExceptionTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    toGenericString = JavaMethod("()Ljava/lang/String;")
    isVarArgs = JavaMethod("()Z")
    isSynthetic = JavaMethod("()Z")
    getParameterAnnotations = JavaMethod("()[[Ljava/lang/annotation/Annotation;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")