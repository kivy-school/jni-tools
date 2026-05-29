from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutputKeys"]

class OutputKeys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/OutputKeys"
    CDATA_SECTION_ELEMENTS = JavaStaticField("Ljava/lang/String;")
    DOCTYPE_PUBLIC = JavaStaticField("Ljava/lang/String;")
    DOCTYPE_SYSTEM = JavaStaticField("Ljava/lang/String;")
    ENCODING = JavaStaticField("Ljava/lang/String;")
    INDENT = JavaStaticField("Ljava/lang/String;")
    MEDIA_TYPE = JavaStaticField("Ljava/lang/String;")
    METHOD = JavaStaticField("Ljava/lang/String;")
    OMIT_XML_DECLARATION = JavaStaticField("Ljava/lang/String;")
    STANDALONE = JavaStaticField("Ljava/lang/String;")
    VERSION = JavaStaticField("Ljava/lang/String;")