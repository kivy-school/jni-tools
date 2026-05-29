from typing import Any, ClassVar, overload
from android.widget.ListAdapter import ListAdapter

class WrapperListAdapter:
    IGNORE_ITEM_VIEW_TYPE: ClassVar[int]
    NO_SELECTION: ClassVar[int]
    def getWrappedAdapter(self) -> ListAdapter: ...
