from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlPullParserFactory"]

class XmlPullParserFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlPullParserFactory"
    PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    newPullParser = JavaMethod("()Lorg/xmlpull/v1/XmlPullParser;")
    newSerializer = JavaMethod("()Lorg/xmlpull/v1/XmlSerializer;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Class;)Lorg/xmlpull/v1/XmlPullParserFactory;", True, False), ("()Lorg/xmlpull/v1/XmlPullParserFactory;", True, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setNamespaceAware = JavaMethod("(Z)V")
    setValidating = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")