from typing import Any, ClassVar, overload
from java.time.temporal.Temporal import Temporal

class TemporalAdjuster:
    def adjustInto(self, p0: Temporal) -> Temporal: ...
