from typing import Any, ClassVar, overload

class LanguageProvider:
    def getLanguage(self) -> str: ...
