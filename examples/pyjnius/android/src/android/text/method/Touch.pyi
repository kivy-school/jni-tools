from typing import Any, ClassVar, overload
from android.text.Layout import Layout
from android.text.Spannable import Spannable
from android.view.MotionEvent import MotionEvent
from android.widget.TextView import TextView

class Touch:
    @staticmethod
    def getInitialScrollY(p0: TextView, p1: Spannable) -> int: ...
    @staticmethod
    def getInitialScrollX(p0: TextView, p1: Spannable) -> int: ...
    @staticmethod
    def scrollTo(p0: TextView, p1: Layout, p2: int, p3: int) -> None: ...
    @staticmethod
    def onTouchEvent(p0: TextView, p1: Spannable, p2: MotionEvent) -> bool: ...
