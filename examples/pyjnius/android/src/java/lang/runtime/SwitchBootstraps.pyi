from typing import Any, ClassVar, overload
from java.lang.invoke.CallSite import CallSite
from java.lang.invoke.MethodType import MethodType

class SwitchBootstraps:
    @staticmethod
    def typeSwitch(p0: Any, p1: str, p2: MethodType, p3: Any) -> CallSite: ...
    @staticmethod
    def enumSwitch(p0: Any, p1: str, p2: MethodType, p3: Any) -> CallSite: ...
