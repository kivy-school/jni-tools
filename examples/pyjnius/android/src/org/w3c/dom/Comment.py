from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Comment"]

class Comment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Comment"
    ELEMENT_NODE = JavaStaticField("S")
    ATTRIBUTE_NODE = JavaStaticField("S")
    TEXT_NODE = JavaStaticField("S")
    CDATA_SECTION_NODE = JavaStaticField("S")
    ENTITY_REFERENCE_NODE = JavaStaticField("S")
    ENTITY_NODE = JavaStaticField("S")
    PROCESSING_INSTRUCTION_NODE = JavaStaticField("S")
    COMMENT_NODE = JavaStaticField("S")
    DOCUMENT_NODE = JavaStaticField("S")
    DOCUMENT_TYPE_NODE = JavaStaticField("S")
    DOCUMENT_FRAGMENT_NODE = JavaStaticField("S")
    NOTATION_NODE = JavaStaticField("S")
    DOCUMENT_POSITION_DISCONNECTED = JavaStaticField("S")
    DOCUMENT_POSITION_PRECEDING = JavaStaticField("S")
    DOCUMENT_POSITION_FOLLOWING = JavaStaticField("S")
    DOCUMENT_POSITION_CONTAINS = JavaStaticField("S")
    DOCUMENT_POSITION_CONTAINED_BY = JavaStaticField("S")
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = JavaStaticField("S")