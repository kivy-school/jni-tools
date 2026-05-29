from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowId"]

class RowId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/RowId"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getBytes = JavaMethod("()[B")