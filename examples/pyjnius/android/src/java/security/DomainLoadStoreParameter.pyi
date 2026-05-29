from typing import Any, ClassVar, overload
from java.net.URI import URI

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ProtectionParameter:
    """Forward declaration for ``java.security.KeyStore.ProtectionParameter``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.security.KeyStore.ProtectionParameter')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/security/KeyStore/ProtectionParameter.html
    """
    ...

class DomainLoadStoreParameter:
    def __init__(self, arg0: URI, arg1: dict) -> None: ...
    def getConfiguration(self) -> URI: ...
    def getProtectionParams(self) -> dict: ...
    def getProtectionParameter(self) -> ProtectionParameter: ...
