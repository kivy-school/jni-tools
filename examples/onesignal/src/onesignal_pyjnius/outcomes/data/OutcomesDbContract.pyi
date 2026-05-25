from typing import Any, ClassVar, overload

class OutcomesDbContract:
    INSTANCE: ClassVar["OutcomesDbContract"]
    OUTCOME_EVENT_TABLE: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_TABLE: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_INFLUENCE_ID: ClassVar[str]
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_TYPE: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V1: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V2: ClassVar[str]
    SQL_CREATE_OUTCOME_ENTRIES_V3: ClassVar[str]
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V1: ClassVar[str]
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V2: ClassVar[str]
