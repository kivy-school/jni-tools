from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMException"]

class DOMException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMException"
    __javaconstructor__ = [("(SLjava/lang/String;)V", False)]
    DOMSTRING_SIZE_ERR = JavaStaticField("S")
    HIERARCHY_REQUEST_ERR = JavaStaticField("S")
    INDEX_SIZE_ERR = JavaStaticField("S")
    INUSE_ATTRIBUTE_ERR = JavaStaticField("S")
    INVALID_ACCESS_ERR = JavaStaticField("S")
    INVALID_CHARACTER_ERR = JavaStaticField("S")
    INVALID_MODIFICATION_ERR = JavaStaticField("S")
    INVALID_STATE_ERR = JavaStaticField("S")
    NAMESPACE_ERR = JavaStaticField("S")
    NOT_FOUND_ERR = JavaStaticField("S")
    NOT_SUPPORTED_ERR = JavaStaticField("S")
    NO_DATA_ALLOWED_ERR = JavaStaticField("S")
    NO_MODIFICATION_ALLOWED_ERR = JavaStaticField("S")
    SYNTAX_ERR = JavaStaticField("S")
    TYPE_MISMATCH_ERR = JavaStaticField("S")
    VALIDATION_ERR = JavaStaticField("S")
    WRONG_DOCUMENT_ERR = JavaStaticField("S")
    code = JavaField("S")