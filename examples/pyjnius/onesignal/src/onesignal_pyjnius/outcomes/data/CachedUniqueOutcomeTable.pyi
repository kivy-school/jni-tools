from typing import Any, ClassVar, overload

class CachedUniqueOutcomeTable:
    INSTANCE: ClassVar["CachedUniqueOutcomeTable"]
    ID: ClassVar[str]
    TABLE_NAME_V2: ClassVar[str]
    TABLE_NAME: ClassVar[str]
    TABLE_NAME_V1: ClassVar[str]
    COLUMN_NAME_NOTIFICATION_ID: ClassVar[str]
    COLUMN_CHANNEL_INFLUENCE_ID: ClassVar[str]
    COLUMN_CHANNEL_TYPE: ClassVar[str]
    COLUMN_NAME_NAME: ClassVar[str]
