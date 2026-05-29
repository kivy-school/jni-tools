from typing import Any, ClassVar, overload

class ListAdapter:
    IGNORE_ITEM_VIEW_TYPE: ClassVar[int]
    NO_SELECTION: ClassVar[int]
    def isEnabled(self, p0: int) -> bool: ...
    def areAllItemsEnabled(self) -> bool: ...
