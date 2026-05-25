from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeVariable"]

class TypeVariable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/TypeVariable"
    getBounds = JavaMethod("()[Ljava/lang/reflect/Type;")
    getGenericDeclaration = JavaMethod("()Ljava/lang/reflect/GenericDeclaration;")
    getName = JavaMethod("()Ljava/lang/String;")