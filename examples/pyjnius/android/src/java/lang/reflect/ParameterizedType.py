from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParameterizedType"]

class ParameterizedType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/ParameterizedType"
    getRawType = JavaMethod("()Ljava/lang/reflect/Type;")
    getActualTypeArguments = JavaMethod("()[Ljava/lang/reflect/Type;")
    getOwnerType = JavaMethod("()Ljava/lang/reflect/Type;")