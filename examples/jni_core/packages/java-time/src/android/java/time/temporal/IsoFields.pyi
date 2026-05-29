from typing import Any, ClassVar, overload
from java.time.temporal.TemporalField import TemporalField
from java.time.temporal.TemporalUnit import TemporalUnit

class IsoFields:
    DAY_OF_QUARTER: ClassVar[TemporalField]
    QUARTER_OF_YEAR: ClassVar[TemporalField]
    WEEK_OF_WEEK_BASED_YEAR: ClassVar[TemporalField]
    WEEK_BASED_YEAR: ClassVar[TemporalField]
    WEEK_BASED_YEARS: ClassVar[TemporalUnit]
    QUARTER_YEARS: ClassVar[TemporalUnit]
