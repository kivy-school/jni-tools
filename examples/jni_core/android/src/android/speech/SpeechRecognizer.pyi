from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.speech.ModelDownloadListener import ModelDownloadListener
from android.speech.RecognitionListener import RecognitionListener
from android.speech.RecognitionSupportCallback import RecognitionSupportCallback
from java.util.concurrent.Executor import Executor

class SpeechRecognizer:
    CONFIDENCE_SCORES: ClassVar[str]
    DETECTED_LANGUAGE: ClassVar[str]
    ERROR_AUDIO: ClassVar[int]
    ERROR_CANNOT_CHECK_SUPPORT: ClassVar[int]
    ERROR_CANNOT_LISTEN_TO_DOWNLOAD_EVENTS: ClassVar[int]
    ERROR_CLIENT: ClassVar[int]
    ERROR_INSUFFICIENT_PERMISSIONS: ClassVar[int]
    ERROR_LANGUAGE_NOT_SUPPORTED: ClassVar[int]
    ERROR_LANGUAGE_UNAVAILABLE: ClassVar[int]
    ERROR_NETWORK: ClassVar[int]
    ERROR_NETWORK_TIMEOUT: ClassVar[int]
    ERROR_NO_MATCH: ClassVar[int]
    ERROR_RECOGNIZER_BUSY: ClassVar[int]
    ERROR_SERVER: ClassVar[int]
    ERROR_SERVER_DISCONNECTED: ClassVar[int]
    ERROR_SPEECH_TIMEOUT: ClassVar[int]
    ERROR_TOO_MANY_REQUESTS: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL: ClassVar[str]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_HIGHLY_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_NOT_CONFIDENT: ClassVar[int]
    LANGUAGE_DETECTION_CONFIDENCE_LEVEL_UNKNOWN: ClassVar[int]
    LANGUAGE_SWITCH_RESULT: ClassVar[str]
    LANGUAGE_SWITCH_RESULT_FAILED: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_NOT_ATTEMPTED: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_SKIPPED_NO_MODEL: ClassVar[int]
    LANGUAGE_SWITCH_RESULT_SUCCEEDED: ClassVar[int]
    RECOGNITION_PARTS: ClassVar[str]
    RESULTS_ALTERNATIVES: ClassVar[str]
    RESULTS_RECOGNITION: ClassVar[str]
    TOP_LOCALE_ALTERNATIVES: ClassVar[str]
    @staticmethod
    def isRecognitionAvailable(p0: Context) -> bool: ...
    @staticmethod
    def isOnDeviceRecognitionAvailable(p0: Context) -> bool: ...
    @overload
    @staticmethod
    def createSpeechRecognizer(p0: Context, p1: ComponentName) -> "SpeechRecognizer": ...
    @overload
    @staticmethod
    def createSpeechRecognizer(p0: Context) -> "SpeechRecognizer": ...
    @staticmethod
    def createOnDeviceSpeechRecognizer(p0: Context) -> "SpeechRecognizer": ...
    def setRecognitionListener(self, p0: RecognitionListener) -> None: ...
    def startListening(self, p0: Intent) -> None: ...
    def stopListening(self) -> None: ...
    def checkRecognitionSupport(self, p0: Intent, p1: Executor, p2: RecognitionSupportCallback) -> None: ...
    @overload
    def triggerModelDownload(self, p0: Intent) -> None: ...
    @overload
    def triggerModelDownload(self, p0: Intent, p1: Executor, p2: ModelDownloadListener) -> None: ...
    def destroy(self) -> None: ...
    def cancel(self) -> None: ...
