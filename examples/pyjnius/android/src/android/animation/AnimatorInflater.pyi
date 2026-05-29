from typing import Any, ClassVar, overload
from android.animation.Animator import Animator
from android.animation.StateListAnimator import StateListAnimator
from android.content.Context import Context

class AnimatorInflater:
    def __init__(self) -> None: ...
    @staticmethod
    def loadAnimator(p0: Context, p1: int) -> Animator: ...
    @staticmethod
    def loadStateListAnimator(p0: Context, p1: int) -> StateListAnimator: ...
