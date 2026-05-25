from typing import Any, ClassVar, overload

class NoCopySpan:

    class Concrete:
        def __init__(self) -> None: ...
