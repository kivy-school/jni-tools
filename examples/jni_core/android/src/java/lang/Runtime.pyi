from typing import Any, ClassVar, overload
from java.lang.invoke.CallSite import CallSite
from java.lang.invoke.MethodType import MethodType

class SwitchBootstraps:
    @staticmethod
    def enumSwitch(p0: Any, p1: str, p2: MethodType, p3: Any) -> CallSite: ...
    @staticmethod
    def typeSwitch(p0: Any, p1: str, p2: MethodType, p3: Any) -> CallSite: ...

from typing import Any, ClassVar, overload
from java.lang.invoke.TypeDescriptor import TypeDescriptor

class ObjectMethods:
    @staticmethod
    def bootstrap(p0: Any, p1: str, p2: TypeDescriptor, p3: type, p4: str, p5: Any) -> Any: ...

