from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Type"]

class Type(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/Type"
    getTypeName = JavaMethod("()Ljava/lang/String;")