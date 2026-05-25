from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Xml"]

class Xml(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Xml"
    FEATURE_RELAXED = JavaStaticField("Ljava/lang/String;")
    parse = JavaMultipleMethod([("(Ljava/lang/String;Lorg/xml/sax/ContentHandler;)V", True, False), ("(Ljava/io/Reader;Lorg/xml/sax/ContentHandler;)V", True, False), ("(Ljava/io/InputStream;Landroid/util/Xml$Encoding;Lorg/xml/sax/ContentHandler;)V", True, False)])
    newPullParser = JavaStaticMethod("()Lorg/xmlpull/v1/XmlPullParser;")
    newSerializer = JavaStaticMethod("()Lorg/xmlpull/v1/XmlSerializer;")
    findEncodingByName = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Xml$Encoding;")
    asAttributeSet = JavaStaticMethod("(Lorg/xmlpull/v1/XmlPullParser;)Landroid/util/AttributeSet;")

    class Encoding(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/util/Xml/Encoding"
        values = JavaStaticMethod("()[Landroid/util/Xml$Encoding;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/Xml$Encoding;")
        US_ASCII = JavaStaticField("Landroid/util/Xml/Encoding;")
        UTF_8 = JavaStaticField("Landroid/util/Xml/Encoding;")
        UTF_16 = JavaStaticField("Landroid/util/Xml/Encoding;")
        ISO_8859_1 = JavaStaticField("Landroid/util/Xml/Encoding;")