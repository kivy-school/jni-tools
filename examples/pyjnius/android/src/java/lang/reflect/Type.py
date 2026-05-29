from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Type"]

class Type(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Type"
    getTypeName = JavaMethod("()Ljava/lang/String;")