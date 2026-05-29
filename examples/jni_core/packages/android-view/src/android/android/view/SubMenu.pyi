from typing import Any, ClassVar, overload
from android.graphics.drawable.Drawable import Drawable
from android.view.MenuItem import MenuItem
from android.view.View import View

class SubMenu:
    CATEGORY_ALTERNATIVE: ClassVar[int]
    CATEGORY_CONTAINER: ClassVar[int]
    CATEGORY_SECONDARY: ClassVar[int]
    CATEGORY_SYSTEM: ClassVar[int]
    FIRST: ClassVar[int]
    FLAG_ALWAYS_PERFORM_CLOSE: ClassVar[int]
    FLAG_APPEND_TO_GROUP: ClassVar[int]
    FLAG_PERFORM_NO_CLOSE: ClassVar[int]
    NONE: ClassVar[int]
    SUPPORTED_MODIFIERS_MASK: ClassVar[int]
    def getItem(self) -> MenuItem: ...
    @overload
    def setIcon(self, p0: int) -> "SubMenu": ...
    @overload
    def setIcon(self, p0: Drawable) -> "SubMenu": ...
    @overload
    def setHeaderTitle(self, p0: int) -> "SubMenu": ...
    @overload
    def setHeaderTitle(self, p0: str) -> "SubMenu": ...
    @overload
    def setHeaderIcon(self, p0: int) -> "SubMenu": ...
    @overload
    def setHeaderIcon(self, p0: Drawable) -> "SubMenu": ...
    def clearHeader(self) -> None: ...
    def setHeaderView(self, p0: View) -> "SubMenu": ...
