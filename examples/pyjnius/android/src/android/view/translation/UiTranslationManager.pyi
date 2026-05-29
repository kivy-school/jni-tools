from typing import Any, ClassVar, overload
from android.view.translation.UiTranslationStateCallback import UiTranslationStateCallback
from java.util.concurrent.Executor import Executor

class UiTranslationManager:
    def registerUiTranslationStateCallback(self, p0: Executor, p1: UiTranslationStateCallback) -> None: ...
    def unregisterUiTranslationStateCallback(self, p0: UiTranslationStateCallback) -> None: ...
