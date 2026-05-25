from typing import Any, ClassVar, overload

class NamedParameterSpec:
    X25519: ClassVar["NamedParameterSpec"]
    X448: ClassVar["NamedParameterSpec"]
    ED25519: ClassVar["NamedParameterSpec"]
    ED448: ClassVar["NamedParameterSpec"]
    def __init__(self, p0: str) -> None: ...
    def getName(self) -> str: ...
