from typing import Any, ClassVar, overload
from android.widget.Filter import Filter

class Filterable:
    def getFilter(self) -> Filter: ...
