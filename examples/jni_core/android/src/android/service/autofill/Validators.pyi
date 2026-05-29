from typing import Any, ClassVar, overload
from android.service.autofill.Validator import Validator

class Validators:
    @staticmethod
    def and_(p0: Any) -> Validator: ...
    @staticmethod
    def not_(p0: Validator) -> Validator: ...
    @staticmethod
    def or_(p0: Any) -> Validator: ...
