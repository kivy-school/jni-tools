from typing import Any, ClassVar, overload

class AgeRestrictedTreatment:
    UNSPECIFIED: ClassVar["AgeRestrictedTreatment"]
    CHILD: ClassVar["AgeRestrictedTreatment"]
    TEEN: ClassVar["AgeRestrictedTreatment"]
    @staticmethod
    def values() -> list["AgeRestrictedTreatment"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AgeRestrictedTreatment": ...
    def getValue(self) -> int: ...
