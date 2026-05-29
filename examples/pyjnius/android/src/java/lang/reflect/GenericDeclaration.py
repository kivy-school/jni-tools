from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GenericDeclaration"]

class GenericDeclaration(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/GenericDeclaration"
    getTypeParameters = JavaMethod("()[Ljava/lang/reflect/TypeVariable;")