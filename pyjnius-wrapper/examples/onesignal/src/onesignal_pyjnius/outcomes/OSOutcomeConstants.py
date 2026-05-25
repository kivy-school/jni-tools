from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSOutcomeConstants"]

class OSOutcomeConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/outcomes/OSOutcomeConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/outcomes/OSOutcomeConstants;")
    PREFS_OS_UNATTRIBUTED_UNIQUE_OUTCOME_EVENTS_SENT = JavaStaticField("Ljava/lang/String;")
    APP_ID = JavaStaticField("Ljava/lang/String;")
    DEVICE_TYPE = JavaStaticField("Ljava/lang/String;")
    DIRECT_PARAM = JavaStaticField("Ljava/lang/String;")
    OUTCOME_ID = JavaStaticField("Ljava/lang/String;")
    OUTCOME_SOURCES = JavaStaticField("Ljava/lang/String;")
    WEIGHT = JavaStaticField("Ljava/lang/String;")
    TIMESTAMP = JavaStaticField("Ljava/lang/String;")
    DIRECT = JavaStaticField("Ljava/lang/String;")
    INDIRECT = JavaStaticField("Ljava/lang/String;")
    NOTIFICATION_IDS = JavaStaticField("Ljava/lang/String;")
    IAM_IDS = JavaStaticField("Ljava/lang/String;")