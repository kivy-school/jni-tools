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
