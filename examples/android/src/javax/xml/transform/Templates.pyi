from typing import Any, ClassVar, overload
from java.util.Properties import Properties
from javax.xml.transform.Transformer import Transformer

class Templates:
    def newTransformer(self) -> Transformer: ...
    def getOutputProperties(self) -> Properties: ...
