from typing import Any, ClassVar, overload

class OSInfluenceConstants:
    INSTANCE: ClassVar["OSInfluenceConstants"]
    TIME: ClassVar[str]
    INFLUENCE_CHANNEL: ClassVar[str]
    INFLUENCE_TYPE: ClassVar[str]
    INFLUENCE_IDS: ClassVar[str]
    IAM_ID_TAG: ClassVar[str]
    DIRECT_TAG: ClassVar[str]
    NOTIFICATIONS_IDS: ClassVar[str]
    NOTIFICATION_ID_TAG: ClassVar[str]
    PREFS_OS_LAST_ATTRIBUTED_NOTIFICATION_OPEN: ClassVar[str]
    PREFS_OS_LAST_NOTIFICATIONS_RECEIVED: ClassVar[str]
    PREFS_OS_LAST_IAMS_RECEIVED: ClassVar[str]
    PREFS_OS_NOTIFICATION_LIMIT: ClassVar[str]
    PREFS_OS_IAM_LIMIT: ClassVar[str]
    PREFS_OS_NOTIFICATION_INDIRECT_ATTRIBUTION_WINDOW: ClassVar[str]
    PREFS_OS_IAM_INDIRECT_ATTRIBUTION_WINDOW: ClassVar[str]
    PREFS_OS_DIRECT_ENABLED: ClassVar[str]
    PREFS_OS_INDIRECT_ENABLED: ClassVar[str]
    PREFS_OS_UNATTRIBUTED_ENABLED: ClassVar[str]
    PREFS_OS_OUTCOMES_CURRENT_NOTIFICATION_INFLUENCE: ClassVar[str]
    PREFS_OS_OUTCOMES_CURRENT_IAM_INFLUENCE: ClassVar[str]
    def getIAM_TAG(self) -> str: ...
    def getNOTIFICATION_TAG(self) -> str: ...
