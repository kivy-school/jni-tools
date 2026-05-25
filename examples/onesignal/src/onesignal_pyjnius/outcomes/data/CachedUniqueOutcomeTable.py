from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CachedUniqueOutcomeTable"]

class CachedUniqueOutcomeTable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/CachedUniqueOutcomeTable"
    INSTANCE = JavaStaticField("Lcom/onesignal/outcomes/data/CachedUniqueOutcomeTable;")
    ID = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME_V2 = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME_V1 = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
    COLUMN_CHANNEL_INFLUENCE_ID = JavaStaticField("Ljava/lang/String;")
    COLUMN_CHANNEL_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NAME = JavaStaticField("Ljava/lang/String;")