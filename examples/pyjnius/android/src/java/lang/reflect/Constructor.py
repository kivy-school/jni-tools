from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Constructor"]

class Constructor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Constructor"
    PUBLIC = JavaStaticField("I")
    DECLARED = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getModifiers = JavaMethod("()I")
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")
    setAccessible = JavaMethod("(Z)V")
    newInstance = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    toGenericString = JavaMethod("()Ljava/lang/String;")
    isSynthetic = JavaMethod("()Z")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    isVarArgs = JavaMethod("()Z")
    getParameterCount = JavaMethod("()I")
    getParameterAnnotations = JavaMethod("()[[Ljava/lang/annotation/Annotation;")
    getGenericParameterTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getGenericExceptionTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getParameterTypes = JavaMethod("()[Ljava/lang/Class;")
    getExceptionTypes = JavaMethod("()[Ljava/lang/Class;")
    getAnnotatedReturnType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")
    getAnnotatedReceiverType = JavaMethod("()Ljava/lang/reflect/AnnotatedType;")