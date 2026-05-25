from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Savepoint"]

class Savepoint(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/Savepoint"
    getSavepointId = JavaMethod("()I")
    getSavepointName = JavaMethod("()Ljava/lang/String;")