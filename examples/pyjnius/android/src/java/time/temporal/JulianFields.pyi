from typing import Any, ClassVar, overload
from java.time.temporal.TemporalField import TemporalField

class JulianFields:
    JULIAN_DAY: ClassVar[TemporalField]
    MODIFIED_JULIAN_DAY: ClassVar[TemporalField]
    RATA_DIE: ClassVar[TemporalField]
