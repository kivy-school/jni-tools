from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnClickListener:
    """Forward declaration for ``android.view.View.OnClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.View.OnClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/View/OnClickListener
    """
    ...
class BackStackEntry:
    """Forward declaration for ``android.app.FragmentManager.BackStackEntry``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.FragmentManager.BackStackEntry')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/FragmentManager/BackStackEntry
    """
    ...

class FragmentBreadCrumbs:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet, arg2: int) -> None: ...
    def setActivity(self, arg0: Activity) -> None: ...
    def setMaxVisible(self, arg0: int) -> None: ...
    def setParentTitle(self, arg0: str, arg1: str, arg2: OnClickListener) -> None: ...
    def setOnBreadCrumbClickListener(self, arg0: "OnBreadCrumbClickListener") -> None: ...
    def setTitle(self, arg0: str, arg1: str) -> None: ...
    def onLayout(self, arg0: bool, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    def onMeasure(self, arg0: int, arg1: int) -> None: ...
    def onBackStackChanged(self) -> None: ...

    class OnBreadCrumbClickListener:
        def onBreadCrumbClick(self, arg0: BackStackEntry, arg1: int) -> bool: ...
