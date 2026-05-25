from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericArrayType"]

class GenericArrayType(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/GenericArrayType"
    getGenericComponentType = JavaMethod("()Ljava/lang/reflect/Type;")