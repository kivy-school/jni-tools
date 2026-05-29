from typing import Any, ClassVar, overload
from android.icu.text.DecimalFormat import DecimalFormat
from android.icu.util.ULocale import ULocale

class ScientificNumberFormatter:
    @overload
    @staticmethod
    def getMarkupInstance(p0: DecimalFormat, p1: str, p2: str) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getMarkupInstance(p0: ULocale, p1: str, p2: str) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getSuperscriptInstance(p0: DecimalFormat) -> "ScientificNumberFormatter": ...
    @overload
    @staticmethod
    def getSuperscriptInstance(p0: ULocale) -> "ScientificNumberFormatter": ...
    def format(self, p0: Any) -> str: ...
