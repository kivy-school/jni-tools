from typing import Any, ClassVar, overload
from android.service.autofill.Validator import Validator

class Validators:
    @staticmethod
    def and_(*arg0: Validator) -> Validator: ...
    @staticmethod
    def or_(*arg0: Validator) -> Validator: ...
    @staticmethod
    def not_(arg0: Validator) -> Validator: ...
