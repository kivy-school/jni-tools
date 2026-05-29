from typing import Any, ClassVar, overload
from android.animation.Animator import Animator
from android.content.Context import Context
from android.transition.TransitionValues import TransitionValues
from android.util.AttributeSet import AttributeSet
from android.view.View import View
from android.view.ViewGroup import ViewGroup

class Fade:
    IN: ClassVar[int]
    OUT: ClassVar[int]
    MODE_IN: ClassVar[int]
    MODE_OUT: ClassVar[int]
    MATCH_ID: ClassVar[int]
    MATCH_INSTANCE: ClassVar[int]
    MATCH_ITEM_ID: ClassVar[int]
    MATCH_NAME: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    def onAppear(self, p0: ViewGroup, p1: View, p2: TransitionValues, p3: TransitionValues) -> Animator: ...
    def onDisappear(self, p0: ViewGroup, p1: View, p2: TransitionValues, p3: TransitionValues) -> Animator: ...
    def captureStartValues(self, p0: TransitionValues) -> None: ...
