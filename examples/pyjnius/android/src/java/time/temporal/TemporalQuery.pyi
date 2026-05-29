from typing import Any, ClassVar, overload
from java.time.temporal.TemporalAccessor import TemporalAccessor

class TemporalQuery:
    def queryFrom(self, p0: TemporalAccessor) -> Any: ...
