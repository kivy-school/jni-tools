from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Struct"]

class Struct(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Struct"
    getSQLTypeName = JavaMethod("()Ljava/lang/String;")
    getAttributes = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("(Ljava/util/Map;)[Ljava/lang/Object;", False, False)])