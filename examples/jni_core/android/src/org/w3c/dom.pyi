from typing import Any, ClassVar, overload
from org.w3c.dom.DOMLocator import DOMLocator

class DOMError:
    SEVERITY_WARNING: ClassVar[int]
    SEVERITY_ERROR: ClassVar[int]
    SEVERITY_FATAL_ERROR: ClassVar[int]
    def getLocation(self) -> DOMLocator: ...
    def getMessage(self) -> str: ...
    def getType(self) -> str: ...
    def getRelatedException(self) -> Any: ...
    def getRelatedData(self) -> Any: ...
    def getSeverity(self) -> int: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class DOMLocator:
    def getLineNumber(self) -> int: ...
    def getByteOffset(self) -> int: ...
    def getUtf16Offset(self) -> int: ...
    def getRelatedNode(self) -> Node: ...
    def getColumnNumber(self) -> int: ...
    def getUri(self) -> str: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Element import Element
from org.w3c.dom.TypeInfo import TypeInfo

class Attr:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getName(self) -> str: ...
    def getValue(self) -> str: ...
    def setValue(self, p0: str) -> None: ...
    def getSpecified(self) -> bool: ...
    def getOwnerElement(self) -> Element: ...
    def getSchemaTypeInfo(self) -> TypeInfo: ...
    def isId(self) -> bool: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.DOMImplementation import DOMImplementation

class DOMImplementationList:
    def getLength(self) -> int: ...
    def item(self, p0: int) -> DOMImplementation: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.DOMStringList import DOMStringList

class DOMConfiguration:
    def canSetParameter(self, p0: str, p1: Any) -> bool: ...
    def getParameterNames(self) -> DOMStringList: ...
    def setParameter(self, p0: str, p1: Any) -> None: ...
    def getParameter(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class UserDataHandler:
    NODE_CLONED: ClassVar[int]
    NODE_IMPORTED: ClassVar[int]
    NODE_DELETED: ClassVar[int]
    NODE_RENAMED: ClassVar[int]
    NODE_ADOPTED: ClassVar[int]
    def handle(self, p0: int, p1: str, p2: Any, p3: Node, p4: Node) -> None: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class NamedNodeMap:
    def getLength(self) -> int: ...
    def getNamedItem(self, p0: str) -> Node: ...
    def setNamedItem(self, p0: Node) -> Node: ...
    def removeNamedItem(self, p0: str) -> Node: ...
    def getNamedItemNS(self, p0: str, p1: str) -> Node: ...
    def setNamedItemNS(self, p0: Node) -> Node: ...
    def removeNamedItemNS(self, p0: str, p1: str) -> Node: ...
    def item(self, p0: int) -> Node: ...

from typing import Any, ClassVar, overload

class CDATASection:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]

from typing import Any, ClassVar, overload
from org.w3c.dom.NamedNodeMap import NamedNodeMap

class DocumentType:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getSystemId(self) -> str: ...
    def getName(self) -> str: ...
    def getEntities(self) -> NamedNodeMap: ...
    def getNotations(self) -> NamedNodeMap: ...
    def getInternalSubset(self) -> str: ...
    def getPublicId(self) -> str: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class NodeList:
    def getLength(self) -> int: ...
    def item(self, p0: int) -> Node: ...

from typing import Any, ClassVar, overload

class DOMException:
    INDEX_SIZE_ERR: ClassVar[int]
    DOMSTRING_SIZE_ERR: ClassVar[int]
    HIERARCHY_REQUEST_ERR: ClassVar[int]
    WRONG_DOCUMENT_ERR: ClassVar[int]
    INVALID_CHARACTER_ERR: ClassVar[int]
    NO_DATA_ALLOWED_ERR: ClassVar[int]
    NO_MODIFICATION_ALLOWED_ERR: ClassVar[int]
    NOT_FOUND_ERR: ClassVar[int]
    NOT_SUPPORTED_ERR: ClassVar[int]
    INUSE_ATTRIBUTE_ERR: ClassVar[int]
    INVALID_STATE_ERR: ClassVar[int]
    SYNTAX_ERR: ClassVar[int]
    INVALID_MODIFICATION_ERR: ClassVar[int]
    NAMESPACE_ERR: ClassVar[int]
    INVALID_ACCESS_ERR: ClassVar[int]
    VALIDATION_ERR: ClassVar[int]
    TYPE_MISMATCH_ERR: ClassVar[int]
    code: int
    def __init__(self, p0: int, p1: str) -> None: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Attr import Attr
from org.w3c.dom.NodeList import NodeList
from org.w3c.dom.TypeInfo import TypeInfo

class Element:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def removeAttribute(self, p0: str) -> None: ...
    def hasAttribute(self, p0: str) -> bool: ...
    def setAttribute(self, p0: str, p1: str) -> None: ...
    def getSchemaTypeInfo(self) -> TypeInfo: ...
    def getAttributeNode(self, p0: str) -> Attr: ...
    def setAttributeNode(self, p0: Attr) -> Attr: ...
    def removeAttributeNode(self, p0: Attr) -> Attr: ...
    def getAttributeNS(self, p0: str, p1: str) -> str: ...
    def setAttributeNS(self, p0: str, p1: str, p2: str) -> None: ...
    def removeAttributeNS(self, p0: str, p1: str) -> None: ...
    def getAttributeNodeNS(self, p0: str, p1: str) -> Attr: ...
    def setAttributeNodeNS(self, p0: Attr) -> Attr: ...
    def hasAttributeNS(self, p0: str, p1: str) -> bool: ...
    def setIdAttribute(self, p0: str, p1: bool) -> None: ...
    def setIdAttributeNS(self, p0: str, p1: str, p2: bool) -> None: ...
    def setIdAttributeNode(self, p0: Attr, p1: bool) -> None: ...
    def getTagName(self) -> str: ...
    def getAttribute(self, p0: str) -> str: ...
    def getElementsByTagName(self, p0: str) -> NodeList: ...
    def getElementsByTagNameNS(self, p0: str, p1: str) -> NodeList: ...

from typing import Any, ClassVar, overload

class Comment:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]

from typing import Any, ClassVar, overload

class TypeInfo:
    DERIVATION_RESTRICTION: ClassVar[int]
    DERIVATION_EXTENSION: ClassVar[int]
    DERIVATION_UNION: ClassVar[int]
    DERIVATION_LIST: ClassVar[int]
    def getTypeName(self) -> str: ...
    def getTypeNamespace(self) -> str: ...
    def isDerivedFrom(self, p0: str, p1: str, p2: int) -> bool: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Document import Document
from org.w3c.dom.DocumentType import DocumentType

class DOMImplementation:
    def createDocument(self, p0: str, p1: str, p2: DocumentType) -> Document: ...
    def getFeature(self, p0: str, p1: str) -> Any: ...
    def hasFeature(self, p0: str, p1: str) -> bool: ...
    def createDocumentType(self, p0: str, p1: str, p2: str) -> DocumentType: ...

from typing import Any, ClassVar, overload

class Notation:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getSystemId(self) -> str: ...
    def getPublicId(self) -> str: ...

from typing import Any, ClassVar, overload

class ProcessingInstruction:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getTarget(self) -> str: ...
    def getData(self) -> str: ...
    def setData(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload

class Entity:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getSystemId(self) -> str: ...
    def getNotationName(self) -> str: ...
    def getInputEncoding(self) -> str: ...
    def getXmlEncoding(self) -> str: ...
    def getXmlVersion(self) -> str: ...
    def getPublicId(self) -> str: ...

from typing import Any, ClassVar, overload

class DocumentFragment:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]

from typing import Any, ClassVar, overload
from org.w3c.dom.DOMImplementation import DOMImplementation
from org.w3c.dom.DOMImplementationList import DOMImplementationList

class DOMImplementationSource:
    def getDOMImplementationList(self, p0: str) -> DOMImplementationList: ...
    def getDOMImplementation(self, p0: str) -> DOMImplementation: ...

from typing import Any, ClassVar, overload

class EntityReference:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]

from typing import Any, ClassVar, overload
from org.w3c.dom.DOMError import DOMError

class DOMErrorHandler:
    def handleError(self, p0: DOMError) -> bool: ...

from typing import Any, ClassVar, overload

class NameList:
    def getName(self, p0: int) -> str: ...
    def getLength(self) -> int: ...
    def contains(self, p0: str) -> bool: ...
    def containsNS(self, p0: str, p1: str) -> bool: ...
    def getNamespaceURI(self, p0: int) -> str: ...

from typing import Any, ClassVar, overload

class Text:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def splitText(self, p0: int) -> "Text": ...
    def isElementContentWhitespace(self) -> bool: ...
    def getWholeText(self) -> str: ...
    def replaceWholeText(self, p0: str) -> "Text": ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Attr import Attr
from org.w3c.dom.CDATASection import CDATASection
from org.w3c.dom.Comment import Comment
from org.w3c.dom.DOMConfiguration import DOMConfiguration
from org.w3c.dom.DOMImplementation import DOMImplementation
from org.w3c.dom.DocumentFragment import DocumentFragment
from org.w3c.dom.DocumentType import DocumentType
from org.w3c.dom.Element import Element
from org.w3c.dom.EntityReference import EntityReference
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList
from org.w3c.dom.ProcessingInstruction import ProcessingInstruction
from org.w3c.dom.Text import Text

class Document:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getInputEncoding(self) -> str: ...
    def getDoctype(self) -> DocumentType: ...
    def getImplementation(self) -> DOMImplementation: ...
    def getDocumentElement(self) -> Element: ...
    def createElement(self, p0: str) -> Element: ...
    def createDocumentFragment(self) -> DocumentFragment: ...
    def createTextNode(self, p0: str) -> Text: ...
    def createComment(self, p0: str) -> Comment: ...
    def createCDATASection(self, p0: str) -> CDATASection: ...
    def createProcessingInstruction(self, p0: str, p1: str) -> ProcessingInstruction: ...
    def createAttribute(self, p0: str) -> Attr: ...
    def createEntityReference(self, p0: str) -> EntityReference: ...
    def getElementsByTagName(self, p0: str) -> NodeList: ...
    def importNode(self, p0: Node, p1: bool) -> Node: ...
    def createElementNS(self, p0: str, p1: str) -> Element: ...
    def createAttributeNS(self, p0: str, p1: str) -> Attr: ...
    def getElementsByTagNameNS(self, p0: str, p1: str) -> NodeList: ...
    def getElementById(self, p0: str) -> Element: ...
    def getXmlEncoding(self) -> str: ...
    def getXmlStandalone(self) -> bool: ...
    def setXmlStandalone(self, p0: bool) -> None: ...
    def getXmlVersion(self) -> str: ...
    def setXmlVersion(self, p0: str) -> None: ...
    def getStrictErrorChecking(self) -> bool: ...
    def setStrictErrorChecking(self, p0: bool) -> None: ...
    def getDocumentURI(self) -> str: ...
    def setDocumentURI(self, p0: str) -> None: ...
    def adoptNode(self, p0: Node) -> Node: ...
    def getDomConfig(self) -> DOMConfiguration: ...
    def normalizeDocument(self) -> None: ...
    def renameNode(self, p0: Node, p1: str, p2: str) -> Node: ...

from typing import Any, ClassVar, overload
from org.w3c.dom.Document import Document
from org.w3c.dom.NamedNodeMap import NamedNodeMap
from org.w3c.dom.NodeList import NodeList
from org.w3c.dom.UserDataHandler import UserDataHandler

class Node:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getUserData(self, p0: str) -> Any: ...
    def setPrefix(self, p0: str) -> None: ...
    def getAttributes(self) -> NamedNodeMap: ...
    def isSupported(self, p0: str, p1: str) -> bool: ...
    def getNamespaceURI(self) -> str: ...
    def setUserData(self, p0: str, p1: Any, p2: UserDataHandler) -> Any: ...
    def removeChild(self, p0: "Node") -> "Node": ...
    def getFeature(self, p0: str, p1: str) -> Any: ...
    def getPrefix(self) -> str: ...
    def compareDocumentPosition(self, p0: "Node") -> int: ...
    def getNextSibling(self) -> "Node": ...
    def getNodeName(self) -> str: ...
    def getNodeValue(self) -> str: ...
    def setNodeValue(self, p0: str) -> None: ...
    def getNodeType(self) -> int: ...
    def getParentNode(self) -> "Node": ...
    def getChildNodes(self) -> NodeList: ...
    def getFirstChild(self) -> "Node": ...
    def getLastChild(self) -> "Node": ...
    def getPreviousSibling(self) -> "Node": ...
    def getOwnerDocument(self) -> Document: ...
    def insertBefore(self, p0: "Node", p1: "Node") -> "Node": ...
    def replaceChild(self, p0: "Node", p1: "Node") -> "Node": ...
    def appendChild(self, p0: "Node") -> "Node": ...
    def hasChildNodes(self) -> bool: ...
    def cloneNode(self, p0: bool) -> "Node": ...
    def hasAttributes(self) -> bool: ...
    def getBaseURI(self) -> str: ...
    def getTextContent(self) -> str: ...
    def setTextContent(self, p0: str) -> None: ...
    def isSameNode(self, p0: "Node") -> bool: ...
    def lookupPrefix(self, p0: str) -> str: ...
    def isDefaultNamespace(self, p0: str) -> bool: ...
    def lookupNamespaceURI(self, p0: str) -> str: ...
    def isEqualNode(self, p0: "Node") -> bool: ...
    def getLocalName(self) -> str: ...
    def normalize(self) -> None: ...

from typing import Any, ClassVar, overload

class CharacterData:
    ELEMENT_NODE: ClassVar[int]
    ATTRIBUTE_NODE: ClassVar[int]
    TEXT_NODE: ClassVar[int]
    CDATA_SECTION_NODE: ClassVar[int]
    ENTITY_REFERENCE_NODE: ClassVar[int]
    ENTITY_NODE: ClassVar[int]
    PROCESSING_INSTRUCTION_NODE: ClassVar[int]
    COMMENT_NODE: ClassVar[int]
    DOCUMENT_NODE: ClassVar[int]
    DOCUMENT_TYPE_NODE: ClassVar[int]
    DOCUMENT_FRAGMENT_NODE: ClassVar[int]
    NOTATION_NODE: ClassVar[int]
    DOCUMENT_POSITION_DISCONNECTED: ClassVar[int]
    DOCUMENT_POSITION_PRECEDING: ClassVar[int]
    DOCUMENT_POSITION_FOLLOWING: ClassVar[int]
    DOCUMENT_POSITION_CONTAINS: ClassVar[int]
    DOCUMENT_POSITION_CONTAINED_BY: ClassVar[int]
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: ClassVar[int]
    def getLength(self) -> int: ...
    def substringData(self, p0: int, p1: int) -> str: ...
    def appendData(self, p0: str) -> None: ...
    def insertData(self, p0: int, p1: str) -> None: ...
    def deleteData(self, p0: int, p1: int) -> None: ...
    def replaceData(self, p0: int, p1: int, p2: str) -> None: ...
    def getData(self) -> str: ...
    def setData(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload

class DOMStringList:
    def getLength(self) -> int: ...
    def contains(self, p0: str) -> bool: ...
    def item(self, p0: int) -> str: ...

