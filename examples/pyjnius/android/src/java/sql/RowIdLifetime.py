from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RowIdLifetime"]

class RowIdLifetime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/RowIdLifetime"
    ROWID_UNSUPPORTED = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_OTHER = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_SESSION = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_TRANSACTION = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_FOREVER = JavaStaticField("Ljava/sql/RowIdLifetime;")
    values = JavaStaticMethod("()[Ljava/sql/RowIdLifetime;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/RowIdLifetime;")
    ROWID_UNSUPPORTED = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_OTHER = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_SESSION = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_TRANSACTION = JavaStaticField("Ljava/sql/RowIdLifetime;")
    ROWID_VALID_FOREVER = JavaStaticField("Ljava/sql/RowIdLifetime;")