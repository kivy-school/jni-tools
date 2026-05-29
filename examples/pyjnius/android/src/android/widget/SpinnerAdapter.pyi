from typing import Any, ClassVar, overload
from android.view.View import View
from android.view.ViewGroup import ViewGroup

class SpinnerAdapter:
    IGNORE_ITEM_VIEW_TYPE: ClassVar[int]
    NO_SELECTION: ClassVar[int]
    def getDropDownView(self, p0: int, p1: View, p2: ViewGroup) -> View: ...
