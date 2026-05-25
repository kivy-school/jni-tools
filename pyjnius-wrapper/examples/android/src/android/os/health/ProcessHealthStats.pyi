from typing import Any, ClassVar, overload

class ProcessHealthStats:
    MEASUREMENT_ANR_COUNT: ClassVar[int]
    MEASUREMENT_CRASHES_COUNT: ClassVar[int]
    MEASUREMENT_FOREGROUND_MS: ClassVar[int]
    MEASUREMENT_STARTS_COUNT: ClassVar[int]
    MEASUREMENT_SYSTEM_TIME_MS: ClassVar[int]
    MEASUREMENT_USER_TIME_MS: ClassVar[int]
