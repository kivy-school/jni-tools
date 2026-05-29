from typing import Any, ClassVar, overload

class SignStyle:
    NORMAL: ClassVar["SignStyle"]
    ALWAYS: ClassVar["SignStyle"]
    NEVER: ClassVar["SignStyle"]
    NOT_NEGATIVE: ClassVar["SignStyle"]
    EXCEEDS_PAD: ClassVar["SignStyle"]
    NORMAL: ClassVar["SignStyle"]
    ALWAYS: ClassVar["SignStyle"]
    NEVER: ClassVar["SignStyle"]
    NOT_NEGATIVE: ClassVar["SignStyle"]
    EXCEEDS_PAD: ClassVar["SignStyle"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "SignStyle": ...
