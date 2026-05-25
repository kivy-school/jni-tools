from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowId"]

class RowId(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/RowId"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getBytes = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")