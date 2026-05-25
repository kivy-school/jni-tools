from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WildcardType"]

class WildcardType(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/WildcardType"
    getUpperBounds = JavaMethod("()[Ljava/lang/reflect/Type;")
    getLowerBounds = JavaMethod("()[Ljava/lang/reflect/Type;")