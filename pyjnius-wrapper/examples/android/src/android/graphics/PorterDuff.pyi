from typing import Any, ClassVar, overload

class PorterDuff:
    def __init__(self) -> None: ...

    class Mode:
        CLEAR: ClassVar["Mode"]
        SRC: ClassVar["Mode"]
        DST: ClassVar["Mode"]
        SRC_OVER: ClassVar["Mode"]
        DST_OVER: ClassVar["Mode"]
        SRC_IN: ClassVar["Mode"]
        DST_IN: ClassVar["Mode"]
        SRC_OUT: ClassVar["Mode"]
        DST_OUT: ClassVar["Mode"]
        SRC_ATOP: ClassVar["Mode"]
        DST_ATOP: ClassVar["Mode"]
        XOR: ClassVar["Mode"]
        DARKEN: ClassVar["Mode"]
        LIGHTEN: ClassVar["Mode"]
        MULTIPLY: ClassVar["Mode"]
        SCREEN: ClassVar["Mode"]
        ADD: ClassVar["Mode"]
        OVERLAY: ClassVar["Mode"]
        @staticmethod
        def values() -> list["Mode"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Mode": ...
