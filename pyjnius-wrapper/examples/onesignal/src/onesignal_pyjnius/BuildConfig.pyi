from typing import Any, ClassVar, overload

class BuildConfig:
    DEBUG: ClassVar[bool]
    LIBRARY_PACKAGE_NAME: ClassVar[str]
    BUILD_TYPE: ClassVar[str]
    def __init__(self) -> None: ...
