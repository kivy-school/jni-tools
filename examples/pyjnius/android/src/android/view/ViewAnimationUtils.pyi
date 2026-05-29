from typing import Any, ClassVar, overload
from android.animation.Animator import Animator
from android.view.View import View

class ViewAnimationUtils:
    @staticmethod
    def createCircularReveal(p0: View, p1: int, p2: int, p3: float, p4: float) -> Animator: ...
