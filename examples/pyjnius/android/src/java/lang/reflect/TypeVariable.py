from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeVariable"]

class TypeVariable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/TypeVariable"
    getName = JavaMethod("()Ljava/lang/String;")
    getBounds = JavaMethod("()[Ljava/lang/reflect/Type;")
    getGenericDeclaration = JavaMethod("()Ljava/lang/reflect/GenericDeclaration;")
    getAnnotatedBounds = JavaMethod("()[Ljava/lang/reflect/AnnotatedType;")