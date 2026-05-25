from typing import Any, ClassVar, overload
from android.media.AudioMetadataMap import AudioMetadataMap

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Key:
    """Forward declaration for ``android.media.AudioMetadata.Key``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.AudioMetadata.Key')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/AudioMetadata/Key
    """
    ...

class AudioMetadataReadMap:
    def containsKey(self, arg0: Key) -> bool: ...
    def dup(self) -> AudioMetadataMap: ...
    def get(self, arg0: Key) -> Any: ...
    def size(self) -> int: ...
