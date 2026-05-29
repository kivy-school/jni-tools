from typing import Any, ClassVar, overload
from java.lang.reflect.Method import Method

class InvocationHandler:
    def invoke(self, p0: Any, p1: Method, p2: Any) -> Any: ...
    @staticmethod
    def invokeDefault(p0: Any, p1: Method, p2: Any) -> Any: ...
