from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutcomeEventsTable"]

class OutcomeEventsTable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/data/OutcomeEventsTable"
    INSTANCE = JavaStaticField("Lcom/onesignal/outcomes/data/OutcomeEventsTable;")
    ID = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_IDS = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_IAM_IDS = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_SESSION = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_IAM_INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NAME = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_WEIGHT = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_TIMESTAMP = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_PARAMS = JavaStaticField("Ljava/lang/String;")