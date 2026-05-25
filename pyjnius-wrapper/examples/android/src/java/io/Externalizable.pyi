from typing import Any, ClassVar, overload
from java.io.ObjectInput import ObjectInput
from java.io.ObjectOutput import ObjectOutput

class Externalizable:
    def writeExternal(self, arg0: ObjectOutput) -> None: ...
    def readExternal(self, arg0: ObjectInput) -> None: ...
