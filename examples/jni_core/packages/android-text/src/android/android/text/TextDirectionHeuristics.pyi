from typing import Any, ClassVar, overload
from android.text.TextDirectionHeuristic import TextDirectionHeuristic

class TextDirectionHeuristics:
    ANYRTL_LTR: ClassVar[TextDirectionHeuristic]
    FIRSTSTRONG_LTR: ClassVar[TextDirectionHeuristic]
    FIRSTSTRONG_RTL: ClassVar[TextDirectionHeuristic]
    LOCALE: ClassVar[TextDirectionHeuristic]
    LTR: ClassVar[TextDirectionHeuristic]
    RTL: ClassVar[TextDirectionHeuristic]
    def __init__(self) -> None: ...
