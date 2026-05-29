from typing import Any, ClassVar, overload

class ThemedSpinnerAdapter:
    IGNORE_ITEM_VIEW_TYPE: ClassVar[int]
    NO_SELECTION: ClassVar[int]
    def getDropDownViewTheme(self) -> Any: ...
    def setDropDownViewTheme(self, p0: Any) -> None: ...
