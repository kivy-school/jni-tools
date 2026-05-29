from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Savepoint"]

class Savepoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Savepoint"
    getSavepointId = JavaMethod("()I")
    getSavepointName = JavaMethod("()Ljava/lang/String;")