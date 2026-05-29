from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.transition.Transition import Transition
from android.transition.TransitionManager import TransitionManager
from android.view.ViewGroup import ViewGroup

class TransitionInflater:
    @staticmethod
    def from_(arg0: Context) -> "TransitionInflater": ...
    def inflateTransition(self, arg0: int) -> Transition: ...
    def inflateTransitionManager(self, arg0: int, arg1: ViewGroup) -> TransitionManager: ...
