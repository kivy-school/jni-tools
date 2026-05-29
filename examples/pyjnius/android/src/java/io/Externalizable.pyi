from typing import Any, ClassVar, overload
from java.io.ObjectInput import ObjectInput
from java.io.ObjectOutput import ObjectOutput

class Externalizable:
    def writeExternal(self, p0: ObjectOutput) -> None: ...
    def readExternal(self, p0: ObjectInput) -> None: ...
