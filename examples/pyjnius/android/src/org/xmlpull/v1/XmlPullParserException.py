from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlPullParserException"]

class XmlPullParserException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlPullParserException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Lorg/xmlpull/v1/XmlPullParser;Ljava/lang/Throwable;)V", False)]
    printStackTrace = JavaMethod("()V")
    getDetail = JavaMethod("()Ljava/lang/Throwable;")
    getColumnNumber = JavaMethod("()I")
    getLineNumber = JavaMethod("()I")