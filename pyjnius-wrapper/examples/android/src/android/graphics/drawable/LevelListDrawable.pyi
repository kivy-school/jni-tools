from typing import Any, ClassVar, overload
from android.content.res.Resources import Resources
from android.graphics.drawable.Drawable import Drawable
from android.util.AttributeSet import AttributeSet
from org.xmlpull.v1.XmlPullParser import XmlPullParser

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Theme:
    """Forward declaration for ``android.content.res.Resources.Theme``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.res.Resources.Theme')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/res/Resources/Theme
    """
    ...
class DrawableContainerState:
    """Forward declaration for ``android.graphics.drawable.DrawableContainer.DrawableContainerState``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.drawable.DrawableContainer.DrawableContainerState')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/drawable/DrawableContainer/DrawableContainerState
    """
    ...

class LevelListDrawable:
    def __init__(self) -> None: ...
    def addLevel(self, arg0: int, arg1: int, arg2: Drawable) -> None: ...
    def onLevelChange(self, arg0: int) -> bool: ...
    def inflate(self, arg0: Resources, arg1: XmlPullParser, arg2: AttributeSet, arg3: Theme) -> None: ...
    def mutate(self) -> Drawable: ...
    def setConstantState(self, arg0: DrawableContainerState) -> None: ...
