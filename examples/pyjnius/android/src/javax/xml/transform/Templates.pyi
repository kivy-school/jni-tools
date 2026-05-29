from typing import Any, ClassVar, overload
from java.util.Properties import Properties
from javax.xml.transform.Transformer import Transformer

class Templates:
    def getOutputProperties(self) -> Properties: ...
    def newTransformer(self) -> Transformer: ...
