from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OptimizationInfo:
    """Forward declaration for ``dalvik.system.DexFile.OptimizationInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('dalvik.system.DexFile.OptimizationInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/dalvik/system/DexFile/OptimizationInfo
    """
    ...

class ApplicationRuntime:
    @staticmethod
    def getBaseApkOptimizationInfo() -> OptimizationInfo: ...
