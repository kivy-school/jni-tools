from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlPullParserFactory"]

class XmlPullParserFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlPullParserFactory"
    __javaconstructor__ = [("()V", False)]
    PROPERTY_NAME = JavaStaticField("Ljava/lang/String;")
    classNamesLocation = JavaField("Ljava/lang/String;")
    features = JavaField("Ljava/util/HashMap;")
    parserClasses = JavaField("Ljava/util/ArrayList;")
    serializerClasses = JavaField("Ljava/util/ArrayList;")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setNamespaceAware = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    setValidating = JavaMethod("(Z)V")
    isValidating = JavaMethod("()Z")
    newPullParser = JavaMethod("()Lorg/xmlpull/v1/XmlPullParser;")
    newSerializer = JavaMethod("()Lorg/xmlpull/v1/XmlSerializer;")
    newInstance = JavaMultipleMethod([("()Lorg/xmlpull/v1/XmlPullParserFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/Class;)Lorg/xmlpull/v1/XmlPullParserFactory;", True, False)])