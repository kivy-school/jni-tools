from typing import Any, ClassVar, overload

class SignStyle:
    NORMAL: ClassVar["SignStyle"]
    ALWAYS: ClassVar["SignStyle"]
    NEVER: ClassVar["SignStyle"]
    NOT_NEGATIVE: ClassVar["SignStyle"]
    EXCEEDS_PAD: ClassVar["SignStyle"]
    @staticmethod
    def values() -> list["SignStyle"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "SignStyle": ...
