from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlResourceParser"]

class XmlResourceParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/XmlResourceParser"
    CDSECT = JavaStaticField("I")
    COMMENT = JavaStaticField("I")
    DOCDECL = JavaStaticField("I")
    END_DOCUMENT = JavaStaticField("I")
    END_TAG = JavaStaticField("I")
    ENTITY_REF = JavaStaticField("I")
    FEATURE_PROCESS_DOCDECL = JavaStaticField("Ljava/lang/String;")
    FEATURE_PROCESS_NAMESPACES = JavaStaticField("Ljava/lang/String;")
    FEATURE_REPORT_NAMESPACE_ATTRIBUTES = JavaStaticField("Ljava/lang/String;")
    FEATURE_VALIDATION = JavaStaticField("Ljava/lang/String;")
    IGNORABLE_WHITESPACE = JavaStaticField("I")
    NO_NAMESPACE = JavaStaticField("Ljava/lang/String;")
    PROCESSING_INSTRUCTION = JavaStaticField("I")
    START_DOCUMENT = JavaStaticField("I")
    START_TAG = JavaStaticField("I")
    TEXT = JavaStaticField("I")
    TYPES = JavaStaticField("[Ljava/lang/String;")
    close = JavaMethod("()V")
    getAttributeNamespace = JavaMethod("(I)Ljava/lang/String;")