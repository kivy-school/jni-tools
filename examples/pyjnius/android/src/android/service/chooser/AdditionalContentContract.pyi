from typing import Any, ClassVar, overload

class AdditionalContentContract:

    class MethodNames:
        ON_SELECTION_CHANGED: ClassVar[str]

    class CursorExtraKeys:
        POSITION: ClassVar[str]

    class Columns:
        URI: ClassVar[str]
