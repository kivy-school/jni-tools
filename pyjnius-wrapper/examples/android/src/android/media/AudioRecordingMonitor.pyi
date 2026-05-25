from typing import Any, ClassVar, overload
from android.media.AudioRecordingConfiguration import AudioRecordingConfiguration
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class AudioRecordingCallback:
    """Forward declaration for ``android.media.AudioManager.AudioRecordingCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.AudioManager.AudioRecordingCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/AudioManager/AudioRecordingCallback
    """
    ...

class AudioRecordingMonitor:
    def registerAudioRecordingCallback(self, arg0: Executor, arg1: AudioRecordingCallback) -> None: ...
    def unregisterAudioRecordingCallback(self, arg0: AudioRecordingCallback) -> None: ...
    def getActiveRecordingConfiguration(self) -> AudioRecordingConfiguration: ...
