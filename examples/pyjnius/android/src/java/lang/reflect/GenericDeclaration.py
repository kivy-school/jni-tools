from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericDeclaration"]

class GenericDeclaration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/GenericDeclaration"
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")