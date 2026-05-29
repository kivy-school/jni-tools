from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericArrayType"]

class GenericArrayType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/GenericArrayType"
    getGenericComponentType = JavaMethod("()Ljava/lang/reflect/Type;")