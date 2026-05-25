from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.transition.Transition import Transition
from android.transition.TransitionManager import TransitionManager
from android.view.ViewGroup import ViewGroup

class TransitionInflater:
    def inflateTransitionManager(self, p0: int, p1: ViewGroup) -> TransitionManager: ...
    def inflateTransition(self, p0: int) -> Transition: ...
    @staticmethod
    def from_(p0: Context) -> "TransitionInflater": ...
