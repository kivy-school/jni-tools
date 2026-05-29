from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect
from android.graphics.Region import Region

class RegionIterator:
    def __init__(self, p0: Region) -> None: ...
    def next(self, p0: Rect) -> bool: ...
