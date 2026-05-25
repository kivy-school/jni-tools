from typing import Any, ClassVar, overload

class OutcomeEventsTable:
    INSTANCE: ClassVar["OutcomeEventsTable"]
    ID: ClassVar[str]
    TABLE_NAME: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_IDS: ClassVar[str]
    COLUMN_NAME_IAM_IDS: ClassVar[str]
    COLUMN_NAME_SESSION: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_INFLUENCE_TYPE: ClassVar[str]
    COLUMN_NAME_IAM_INFLUENCE_TYPE: ClassVar[str]
    COLUMN_NAME_NAME: ClassVar[str]
    COLUMN_NAME_WEIGHT: ClassVar[str]
    COLUMN_NAME_TIMESTAMP: ClassVar[str]
    COLUMN_NAME_PARAMS: ClassVar[str]
