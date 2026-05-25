from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Session:
    """Forward declaration for ``android.media.MediaCas.Session``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.MediaCas.Session')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/MediaCas/Session
    """
    ...
class CryptoInfo:
    """Forward declaration for ``android.media.MediaCodec.CryptoInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.MediaCodec.CryptoInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/MediaCodec/CryptoInfo
    """
    ...

class MediaDescrambler:
    SCRAMBLE_CONTROL_EVEN_KEY: ClassVar[int]
    SCRAMBLE_CONTROL_ODD_KEY: ClassVar[int]
    SCRAMBLE_CONTROL_RESERVED: ClassVar[int]
    SCRAMBLE_CONTROL_UNSCRAMBLED: ClassVar[int]
    SCRAMBLE_FLAG_PES_HEADER: ClassVar[int]
    def __init__(self, arg0: int) -> None: ...
    def requiresSecureDecoderComponent(self, arg0: str) -> bool: ...
    def setMediaCasSession(self, arg0: Session) -> None: ...
    def descramble(self, arg0: ByteBuffer, arg1: ByteBuffer, arg2: CryptoInfo) -> int: ...
    def close(self) -> None: ...
    def finalize(self) -> None: ...
