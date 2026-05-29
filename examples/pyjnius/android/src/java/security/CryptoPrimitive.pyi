from typing import Any, ClassVar, overload

class CryptoPrimitive:
    MESSAGE_DIGEST: ClassVar["CryptoPrimitive"]
    SECURE_RANDOM: ClassVar["CryptoPrimitive"]
    BLOCK_CIPHER: ClassVar["CryptoPrimitive"]
    STREAM_CIPHER: ClassVar["CryptoPrimitive"]
    MAC: ClassVar["CryptoPrimitive"]
    KEY_WRAP: ClassVar["CryptoPrimitive"]
    PUBLIC_KEY_ENCRYPTION: ClassVar["CryptoPrimitive"]
    SIGNATURE: ClassVar["CryptoPrimitive"]
    KEY_ENCAPSULATION: ClassVar["CryptoPrimitive"]
    KEY_AGREEMENT: ClassVar["CryptoPrimitive"]
    MESSAGE_DIGEST: ClassVar["CryptoPrimitive"]
    SECURE_RANDOM: ClassVar["CryptoPrimitive"]
    BLOCK_CIPHER: ClassVar["CryptoPrimitive"]
    STREAM_CIPHER: ClassVar["CryptoPrimitive"]
    MAC: ClassVar["CryptoPrimitive"]
    KEY_WRAP: ClassVar["CryptoPrimitive"]
    PUBLIC_KEY_ENCRYPTION: ClassVar["CryptoPrimitive"]
    SIGNATURE: ClassVar["CryptoPrimitive"]
    KEY_ENCAPSULATION: ClassVar["CryptoPrimitive"]
    KEY_AGREEMENT: ClassVar["CryptoPrimitive"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "CryptoPrimitive": ...
