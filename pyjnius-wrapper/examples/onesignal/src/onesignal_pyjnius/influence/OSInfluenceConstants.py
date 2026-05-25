from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInfluenceConstants"]

class OSInfluenceConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/influence/OSInfluenceConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/influence/OSInfluenceConstants;")
    TIME = JavaStaticField("Ljava/lang/String;")
    INFLUENCE_CHANNEL = JavaStaticField("Ljava/lang/String;")
    INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    INFLUENCE_IDS = JavaStaticField("Ljava/lang/String;")
    IAM_ID_TAG = JavaStaticField("Ljava/lang/String;")
    DIRECT_TAG = JavaStaticField("Ljava/lang/String;")
    NOTIFICATIONS_IDS = JavaStaticField("Ljava/lang/String;")
    NOTIFICATION_ID_TAG = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_LAST_ATTRIBUTED_NOTIFICATION_OPEN = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_LAST_NOTIFICATIONS_RECEIVED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_LAST_IAMS_RECEIVED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_NOTIFICATION_LIMIT = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_IAM_LIMIT = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_NOTIFICATION_INDIRECT_ATTRIBUTION_WINDOW = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_IAM_INDIRECT_ATTRIBUTION_WINDOW = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_DIRECT_ENABLED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_INDIRECT_ENABLED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_UNATTRIBUTED_ENABLED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_OUTCOMES_CURRENT_NOTIFICATION_INFLUENCE = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_OUTCOMES_CURRENT_IAM_INFLUENCE = JavaStaticField("Ljava/lang/String;")
    getIAM_TAG = JavaMethod("()Ljava/lang/String;")
    getNOTIFICATION_TAG = JavaMethod("()Ljava/lang/String;")