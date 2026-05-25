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
    @staticmethod
    def values() -> list["CryptoPrimitive"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "CryptoPrimitive": ...
