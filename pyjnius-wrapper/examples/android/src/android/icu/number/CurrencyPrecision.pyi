from typing import Any, ClassVar, overload
from android.icu.number.Precision import Precision
from android.icu.util.Currency import Currency

class CurrencyPrecision:
    def withCurrency(self, arg0: Currency) -> Precision: ...
