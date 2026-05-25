from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLConstants"]

class XMLConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/XMLConstants"
    DEFAULT_NS_PREFIX = JavaStaticField("Ljava/lang/String;")
    FEATURE_SECURE_PROCESSING = JavaStaticField("Ljava/lang/String;")
    NULL_NS_URI = JavaStaticField("Ljava/lang/String;")
    RELAXNG_NS_URI = JavaStaticField("Ljava/lang/String;")
    W3C_XML_SCHEMA_INSTANCE_NS_URI = JavaStaticField("Ljava/lang/String;")
    W3C_XML_SCHEMA_NS_URI = JavaStaticField("Ljava/lang/String;")
    W3C_XPATH_DATATYPE_NS_URI = JavaStaticField("Ljava/lang/String;")
    XMLNS_ATTRIBUTE = JavaStaticField("Ljava/lang/String;")
    XMLNS_ATTRIBUTE_NS_URI = JavaStaticField("Ljava/lang/String;")
    XML_DTD_NS_URI = JavaStaticField("Ljava/lang/String;")
    XML_NS_PREFIX = JavaStaticField("Ljava/lang/String;")
    XML_NS_URI = JavaStaticField("Ljava/lang/String;")