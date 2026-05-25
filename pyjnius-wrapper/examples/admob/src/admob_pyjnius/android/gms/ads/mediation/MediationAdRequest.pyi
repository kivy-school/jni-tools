from typing import Any, ClassVar, overload
from android.location.Location import Location

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Date:
    """Forward declaration for ``java.util.Date``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Date')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Date.html
    """
    ...

class MediationAdRequest:
    TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE: ClassVar[int]
    TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE: ClassVar[int]
    TAG_FOR_CHILD_DIRECTED_TREATMENT_UNSPECIFIED: ClassVar[int]
    def getBirthday(self) -> Date: ...
    def getGender(self) -> int: ...
    def getKeywords(self) -> set: ...
    def getLocation(self) -> Location: ...
    def taggedForChildDirectedTreatment(self) -> int: ...
    def isTesting(self) -> bool: ...
    def isDesignedForFamilies(self) -> bool: ...
