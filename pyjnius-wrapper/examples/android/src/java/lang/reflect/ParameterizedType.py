from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParameterizedType"]

class ParameterizedType(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/ParameterizedType"
    getActualTypeArguments = JavaMethod("()[Ljava/lang/reflect/Type;")
    getRawType = JavaMethod("()Ljava/lang/reflect/Type;")
    getOwnerType = JavaMethod("()Ljava/lang/reflect/Type;")