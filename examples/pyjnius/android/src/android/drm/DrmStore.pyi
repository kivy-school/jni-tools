from typing import Any, ClassVar, overload

class DrmStore:
    def __init__(self) -> None: ...

    class RightsStatus:
        RIGHTS_EXPIRED: ClassVar[int]
        RIGHTS_INVALID: ClassVar[int]
        RIGHTS_NOT_ACQUIRED: ClassVar[int]
        RIGHTS_VALID: ClassVar[int]
        def __init__(self) -> None: ...

    class Playback:
        PAUSE: ClassVar[int]
        RESUME: ClassVar[int]
        START: ClassVar[int]
        STOP: ClassVar[int]
        def __init__(self) -> None: ...

    class DrmObjectType:
        CONTENT: ClassVar[int]
        RIGHTS_OBJECT: ClassVar[int]
        TRIGGER_OBJECT: ClassVar[int]
        UNKNOWN: ClassVar[int]
        def __init__(self) -> None: ...

    class ConstraintsColumns:
        EXTENDED_METADATA: ClassVar[str]
        LICENSE_AVAILABLE_TIME: ClassVar[str]
        LICENSE_EXPIRY_TIME: ClassVar[str]
        LICENSE_START_TIME: ClassVar[str]
        MAX_REPEAT_COUNT: ClassVar[str]
        REMAINING_REPEAT_COUNT: ClassVar[str]

    class Action:
        DEFAULT: ClassVar[int]
        DISPLAY: ClassVar[int]
        EXECUTE: ClassVar[int]
        OUTPUT: ClassVar[int]
        PLAY: ClassVar[int]
        PREVIEW: ClassVar[int]
        RINGTONE: ClassVar[int]
        TRANSFER: ClassVar[int]
        def __init__(self) -> None: ...
