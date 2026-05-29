from typing import Any, ClassVar, overload
from android.view.translation.UiTranslationStateCallback import UiTranslationStateCallback
from java.util.concurrent.Executor import Executor

class UiTranslationManager:
    def registerUiTranslationStateCallback(self, arg0: Executor, arg1: UiTranslationStateCallback) -> None: ...
    def unregisterUiTranslationStateCallback(self, arg0: UiTranslationStateCallback) -> None: ...
