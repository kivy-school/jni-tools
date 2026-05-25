from typing import Any, ClassVar, overload
from android.widget.ListAdapter import ListAdapter

class WrapperListAdapter:
    def getWrappedAdapter(self) -> ListAdapter: ...
