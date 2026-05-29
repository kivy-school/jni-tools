from typing import Any, ClassVar, overload
from java.security.spec.NamedParameterSpec import NamedParameterSpec

class ECGenParameterSpec:
    X25519: ClassVar[NamedParameterSpec]
    X448: ClassVar[NamedParameterSpec]
    ED25519: ClassVar[NamedParameterSpec]
    ED448: ClassVar[NamedParameterSpec]
    def __init__(self, p0: str) -> None: ...
