from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClientInfoStatus"]

class ClientInfoStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/sql/ClientInfoStatus"
    REASON_UNKNOWN = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_UNKNOWN_PROPERTY = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_VALUE_INVALID = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_VALUE_TRUNCATED = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    values = JavaStaticMethod("()[Ljava/sql/ClientInfoStatus;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/sql/ClientInfoStatus;")
    REASON_UNKNOWN = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_UNKNOWN_PROPERTY = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_VALUE_INVALID = JavaStaticField("Ljava/sql/ClientInfoStatus;")
    REASON_VALUE_TRUNCATED = JavaStaticField("Ljava/sql/ClientInfoStatus;")