from typing import Any, ClassVar, overload

class AdditionalContentContract:

    class Columns:
        URI: ClassVar[str]

    class CursorExtraKeys:
        POSITION: ClassVar[str]

    class MethodNames:
        ON_SELECTION_CHANGED: ClassVar[str]
