from typing import Any, ClassVar, overload
from java.time.temporal.TemporalAccessor import TemporalAccessor

class TemporalQuery:
    def queryFrom(self, arg0: TemporalAccessor) -> Any: ...
