from typing import Any, ClassVar, overload
from android.text.Layout import Layout
from android.text.Spannable import Spannable
from android.view.MotionEvent import MotionEvent
from android.widget.TextView import TextView

class Touch:
    @staticmethod
    def scrollTo(arg0: TextView, arg1: Layout, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def onTouchEvent(arg0: TextView, arg1: Spannable, arg2: MotionEvent) -> bool: ...
    @staticmethod
    def getInitialScrollX(arg0: TextView, arg1: Spannable) -> int: ...
    @staticmethod
    def getInitialScrollY(arg0: TextView, arg1: Spannable) -> int: ...
