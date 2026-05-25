from typing import Any, ClassVar, overload
from android.content.ContentResolver import ContentResolver
from android.content.Context import Context

class SearchRecentSuggestions:
    QUERIES_PROJECTION_1LINE: ClassVar[list[str]]
    QUERIES_PROJECTION_2LINE: ClassVar[list[str]]
    QUERIES_PROJECTION_DATE_INDEX: ClassVar[int]
    QUERIES_PROJECTION_DISPLAY1_INDEX: ClassVar[int]
    QUERIES_PROJECTION_DISPLAY2_INDEX: ClassVar[int]
    QUERIES_PROJECTION_QUERY_INDEX: ClassVar[int]
    def __init__(self, arg0: Context, arg1: str, arg2: int) -> None: ...
    def saveRecentQuery(self, arg0: str, arg1: str) -> None: ...
    def clearHistory(self) -> None: ...
    def truncateHistory(self, arg0: ContentResolver, arg1: int) -> None: ...
