from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Builder:
    """Forward declaration for ``java.security.KeyStore.Builder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.security.KeyStore.Builder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/security/KeyStore/Builder.html
    """
    ...

class KeyStoreBuilderParameters:
    @overload
    def __init__(self, arg0: Builder) -> None: ...
    @overload
    def __init__(self, arg0: list) -> None: ...
    def getParameters(self) -> list: ...
