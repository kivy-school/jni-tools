from typing import Any, ClassVar, overload

class IkeSaProposal:
    DH_GROUP_1024_BIT_MODP: ClassVar[int]
    DH_GROUP_1536_BIT_MODP: ClassVar[int]
    DH_GROUP_2048_BIT_MODP: ClassVar[int]
    DH_GROUP_3072_BIT_MODP: ClassVar[int]
    DH_GROUP_4096_BIT_MODP: ClassVar[int]
    DH_GROUP_CURVE_25519: ClassVar[int]
    DH_GROUP_NONE: ClassVar[int]
    ENCRYPTION_ALGORITHM_3DES: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES_CBC: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES_CTR: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES_GCM_12: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES_GCM_16: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES_GCM_8: ClassVar[int]
    ENCRYPTION_ALGORITHM_CHACHA20_POLY1305: ClassVar[int]
    INTEGRITY_ALGORITHM_AES_CMAC_96: ClassVar[int]
    INTEGRITY_ALGORITHM_AES_XCBC_96: ClassVar[int]
    INTEGRITY_ALGORITHM_HMAC_SHA1_96: ClassVar[int]
    INTEGRITY_ALGORITHM_HMAC_SHA2_256_128: ClassVar[int]
    INTEGRITY_ALGORITHM_HMAC_SHA2_384_192: ClassVar[int]
    INTEGRITY_ALGORITHM_HMAC_SHA2_512_256: ClassVar[int]
    INTEGRITY_ALGORITHM_NONE: ClassVar[int]
    KEY_LEN_AES_128: ClassVar[int]
    KEY_LEN_AES_192: ClassVar[int]
    KEY_LEN_AES_256: ClassVar[int]
    KEY_LEN_UNUSED: ClassVar[int]
    PSEUDORANDOM_FUNCTION_AES128_CMAC: ClassVar[int]
    PSEUDORANDOM_FUNCTION_AES128_XCBC: ClassVar[int]
    PSEUDORANDOM_FUNCTION_HMAC_SHA1: ClassVar[int]
    PSEUDORANDOM_FUNCTION_SHA2_256: ClassVar[int]
    PSEUDORANDOM_FUNCTION_SHA2_384: ClassVar[int]
    PSEUDORANDOM_FUNCTION_SHA2_512: ClassVar[int]
    @staticmethod
    def getSupportedEncryptionAlgorithms() -> set: ...
    @staticmethod
    def getSupportedIntegrityAlgorithms() -> set: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def getSupportedPseudorandomFunctions() -> set: ...
    def getPseudorandomFunctions(self) -> list: ...

    class Builder:
        def __init__(self) -> None: ...
        def addDhGroup(self, p0: int) -> Any: ...
        def addEncryptionAlgorithm(self, p0: int, p1: int) -> Any: ...
        def addIntegrityAlgorithm(self, p0: int) -> Any: ...
        def addPseudorandomFunction(self, p0: int) -> Any: ...
        def build(self) -> "IkeSaProposal": ...
