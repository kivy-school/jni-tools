from typing import Any, ClassVar, overload
from java.lang.reflect.Method import Method

class InvocationHandler:
    def invoke(self, arg0: Any, arg1: Method, arg2: list) -> Any: ...
