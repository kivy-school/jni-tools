from typing import Any, ClassVar, overload

class MGF1ParameterSpec:
    SHA1: ClassVar["MGF1ParameterSpec"]
    SHA224: ClassVar["MGF1ParameterSpec"]
    SHA256: ClassVar["MGF1ParameterSpec"]
    SHA384: ClassVar["MGF1ParameterSpec"]
    SHA512: ClassVar["MGF1ParameterSpec"]
    SHA512_224: ClassVar["MGF1ParameterSpec"]
    SHA512_256: ClassVar["MGF1ParameterSpec"]
    SHA3_224: ClassVar["MGF1ParameterSpec"]
    SHA3_256: ClassVar["MGF1ParameterSpec"]
    SHA3_384: ClassVar["MGF1ParameterSpec"]
    SHA3_512: ClassVar["MGF1ParameterSpec"]
    def __init__(self, p0: str) -> None: ...
    def toString(self) -> str: ...
    def getDigestAlgorithm(self) -> str: ...
