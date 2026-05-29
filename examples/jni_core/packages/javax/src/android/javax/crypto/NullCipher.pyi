from typing import Any, ClassVar, overload

class NullCipher:
    ENCRYPT_MODE: ClassVar[int]
    DECRYPT_MODE: ClassVar[int]
    WRAP_MODE: ClassVar[int]
    UNWRAP_MODE: ClassVar[int]
    PUBLIC_KEY: ClassVar[int]
    PRIVATE_KEY: ClassVar[int]
    SECRET_KEY: ClassVar[int]
    def __init__(self) -> None: ...
