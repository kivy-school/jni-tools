from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutcomesDbContract"]

class OutcomesDbContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OutcomesDbContract"
    INSTANCE = JavaStaticField("Lcom/onesignal/outcomes/data/OutcomesDbContract;")
    OUTCOME_EVENT_TABLE = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_TABLE = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_INFLUENCE_ID = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_TYPE = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V1 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V2 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V3 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V1 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V2 = JavaStaticField("Ljava/lang/String;")