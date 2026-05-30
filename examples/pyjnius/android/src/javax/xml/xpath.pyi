from typing import Any, ClassVar, overload

class XPathFunction:
    def evaluate(self, p0: list) -> Any: ...

from typing import Any, ClassVar, overload
from javax.xml.namespace.NamespaceContext import NamespaceContext
from javax.xml.namespace.QName import QName
from javax.xml.xpath.XPathExpression import XPathExpression
from javax.xml.xpath.XPathFunctionResolver import XPathFunctionResolver
from javax.xml.xpath.XPathVariableResolver import XPathVariableResolver
from org.xml.sax.InputSource import InputSource

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class XPathEvaluationResult:
    """Forward declaration for ``javax.xml.xpath.XPathEvaluationResult``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('javax.xml.xpath.XPathEvaluationResult')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/javax/xml/xpath/XPathEvaluationResult.html
    """
    ...

class XPath:
    @overload
    def evaluate(self, p0: str, p1: Any) -> str: ...
    @overload
    def evaluate(self, p0: str, p1: InputSource, p2: QName) -> Any: ...
    @overload
    def evaluate(self, p0: str, p1: InputSource) -> str: ...
    @overload
    def evaluate(self, p0: str, p1: Any, p2: QName) -> Any: ...
    @overload
    def evaluateExpression(self, p0: str, p1: InputSource) -> XPathEvaluationResult: ...
    @overload
    def evaluateExpression(self, p0: str, p1: InputSource, p2: type) -> Any: ...
    @overload
    def evaluateExpression(self, p0: str, p1: Any) -> XPathEvaluationResult: ...
    @overload
    def evaluateExpression(self, p0: str, p1: Any, p2: type) -> Any: ...
    def setXPathVariableResolver(self, p0: XPathVariableResolver) -> None: ...
    def getXPathVariableResolver(self) -> XPathVariableResolver: ...
    def setXPathFunctionResolver(self, p0: XPathFunctionResolver) -> None: ...
    def getXPathFunctionResolver(self) -> XPathFunctionResolver: ...
    def setNamespaceContext(self, p0: NamespaceContext) -> None: ...
    def getNamespaceContext(self) -> NamespaceContext: ...
    def reset(self) -> None: ...
    def compile(self, p0: str) -> XPathExpression: ...

from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from javax.xml.xpath.XPath import XPath
from javax.xml.xpath.XPathFunctionResolver import XPathFunctionResolver
from javax.xml.xpath.XPathVariableResolver import XPathVariableResolver

class XPathFactory:
    DEFAULT_PROPERTY_NAME: ClassVar[str]
    DEFAULT_OBJECT_MODEL_URI: ClassVar[str]
    def setXPathVariableResolver(self, p0: XPathVariableResolver) -> None: ...
    def setXPathFunctionResolver(self, p0: XPathFunctionResolver) -> None: ...
    def isObjectModelSupported(self, p0: str) -> bool: ...
    def newXPath(self) -> XPath: ...
    def getProperty(self, p0: str) -> str: ...
    @overload
    @staticmethod
    def newInstance() -> "XPathFactory": ...
    @overload
    @staticmethod
    def newInstance(p0: str) -> "XPathFactory": ...
    @overload
    @staticmethod
    def newInstance(p0: str, p1: str, p2: ClassLoader) -> "XPathFactory": ...
    def setProperty(self, p0: str, p1: str) -> None: ...
    def getFeature(self, p0: str) -> bool: ...
    def setFeature(self, p0: str, p1: bool) -> None: ...
    @staticmethod
    def newDefaultInstance() -> "XPathFactory": ...

from typing import Any, ClassVar, overload
from java.io.PrintStream import PrintStream
from java.io.PrintWriter import PrintWriter
from java.lang.Throwable import Throwable

class XPathException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def printStackTrace(self, p0: PrintWriter) -> None: ...
    @overload
    def printStackTrace(self, p0: PrintStream) -> None: ...
    @overload
    def printStackTrace(self) -> None: ...
    def getCause(self) -> Throwable: ...

from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName
from javax.xml.xpath.XPathFunction import XPathFunction

class XPathFunctionResolver:
    def resolveFunction(self, p0: QName, p1: int) -> XPathFunction: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class XPathExpressionException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...

from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class XPathVariableResolver:
    def resolveVariable(self, p0: QName) -> Any: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class XPathFactoryConfigurationException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class XPathFunctionException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...

from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName
from org.xml.sax.InputSource import InputSource

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class XPathEvaluationResult:
    """Forward declaration for ``javax.xml.xpath.XPathEvaluationResult``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('javax.xml.xpath.XPathEvaluationResult')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/javax/xml/xpath/XPathEvaluationResult.html
    """
    ...

class XPathExpression:
    @overload
    def evaluate(self, p0: InputSource) -> str: ...
    @overload
    def evaluate(self, p0: InputSource, p1: QName) -> Any: ...
    @overload
    def evaluate(self, p0: Any) -> str: ...
    @overload
    def evaluate(self, p0: Any, p1: QName) -> Any: ...
    @overload
    def evaluateExpression(self, p0: InputSource, p1: type) -> Any: ...
    @overload
    def evaluateExpression(self, p0: InputSource) -> XPathEvaluationResult: ...
    @overload
    def evaluateExpression(self, p0: Any) -> XPathEvaluationResult: ...
    @overload
    def evaluateExpression(self, p0: Any, p1: type) -> Any: ...

from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class XPathConstants:
    NUMBER: ClassVar[QName]
    STRING: ClassVar[QName]
    BOOLEAN: ClassVar[QName]
    NODESET: ClassVar[QName]
    NODE: ClassVar[QName]
    DOM_OBJECT_MODEL: ClassVar[str]

