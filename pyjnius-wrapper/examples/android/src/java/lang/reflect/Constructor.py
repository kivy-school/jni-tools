from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Constructor"]

class Constructor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Constructor"
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    getName = JavaMethod("()Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")
    getParameterTypes = JavaMethod("()[Ljava/lang/Class;")
    getParameterCount = JavaMethod("()I")
    getGenericParameterTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    getExceptionTypes = JavaMethod("()[Ljava/lang/Class;")
    getGenericExceptionTypes = JavaMethod("()[Ljava/lang/reflect/Type;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    toGenericString = JavaMethod("()Ljava/lang/String;")
    newInstance = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    isVarArgs = JavaMethod("()Z")
    isSynthetic = JavaMethod("()Z")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getParameterAnnotations = JavaMethod("()[[Ljava/lang/annotation/Annotation;")