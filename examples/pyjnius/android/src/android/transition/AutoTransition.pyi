from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet

class AutoTransition:
    ORDERING_SEQUENTIAL: ClassVar[int]
    ORDERING_TOGETHER: ClassVar[int]
    MATCH_ID: ClassVar[int]
    MATCH_INSTANCE: ClassVar[int]
    MATCH_ITEM_ID: ClassVar[int]
    MATCH_NAME: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
