from typing import Any, ClassVar, overload
from android.icu.text.DecimalFormat import DecimalFormat
from android.icu.util.ULocale import ULocale

class ScientificNumberFormatter:
    @overload
    @staticmethod
    def getSuperscriptInstance(arg0: ULocale) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getSuperscriptInstance(arg0: DecimalFormat) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getMarkupInstance(arg0: ULocale, arg1: str, arg2: str) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getMarkupInstance(arg0: DecimalFormat, arg1: str, arg2: str) -> "ScientificNumberFormatter": ...
    def format(self, arg0: Any) -> str: ...
