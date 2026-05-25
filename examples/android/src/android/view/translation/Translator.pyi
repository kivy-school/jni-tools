from typing import Any, ClassVar, overload
from android.os.CancellationSignal import CancellationSignal
from android.view.translation.TranslationRequest import TranslationRequest
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class Translator:
    def translate(self, arg0: TranslationRequest, arg1: CancellationSignal, arg2: Executor, arg3: Consumer) -> None: ...
    def destroy(self) -> None: ...
    def isDestroyed(self) -> bool: ...
