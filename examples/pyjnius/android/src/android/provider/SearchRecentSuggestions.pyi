from typing import Any, ClassVar, overload
from android.content.Context import Context

class SearchRecentSuggestions:
    QUERIES_PROJECTION_1LINE: ClassVar[Any]
    QUERIES_PROJECTION_2LINE: ClassVar[Any]
    QUERIES_PROJECTION_DATE_INDEX: ClassVar[int]
    QUERIES_PROJECTION_DISPLAY1_INDEX: ClassVar[int]
    QUERIES_PROJECTION_DISPLAY2_INDEX: ClassVar[int]
    QUERIES_PROJECTION_QUERY_INDEX: ClassVar[int]
    def __init__(self, p0: Context, p1: str, p2: int) -> None: ...
    def saveRecentQuery(self, p0: str, p1: str) -> None: ...
    def clearHistory(self) -> None: ...
