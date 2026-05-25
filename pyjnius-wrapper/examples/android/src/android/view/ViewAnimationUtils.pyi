from typing import Any, ClassVar, overload
from android.animation.Animator import Animator
from android.view.View import View

class ViewAnimationUtils:
    @staticmethod
    def createCircularReveal(arg0: View, arg1: int, arg2: int, arg3: float, arg4: float) -> Animator: ...
