from typing import Any, ClassVar, overload
from javax.xml.transform.Source import Source
from javax.xml.transform.Templates import Templates
from javax.xml.transform.sax.TemplatesHandler import TemplatesHandler
from javax.xml.transform.sax.TransformerHandler import TransformerHandler
from org.xml.sax.XMLFilter import XMLFilter

class SAXTransformerFactory:
    FEATURE: ClassVar[str]
    FEATURE_XMLFILTER: ClassVar[str]
    @overload
    def newTransformerHandler(self) -> TransformerHandler: ...
    @overload
    def newTransformerHandler(self, p0: Templates) -> TransformerHandler: ...
    @overload
    def newTransformerHandler(self, p0: Source) -> TransformerHandler: ...
    def newTemplatesHandler(self) -> TemplatesHandler: ...
    @overload
    def newXMLFilter(self, p0: Templates) -> XMLFilter: ...
    @overload
    def newXMLFilter(self, p0: Source) -> XMLFilter: ...
