from typing import Any, ClassVar, overload
from android.os.CancellationSignal import CancellationSignal
from android.view.translation.TranslationRequest import TranslationRequest
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class Translator:
    def translate(self, p0: TranslationRequest, p1: CancellationSignal, p2: Executor, p3: Consumer) -> None: ...
    def isDestroyed(self) -> bool: ...
    def destroy(self) -> None: ...
