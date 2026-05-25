from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XmlPullParserException"]

class XmlPullParserException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/XmlPullParserException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Lorg/xmlpull/v1/XmlPullParser;Ljava/lang/Throwable;)V", False)]
    column = JavaField("I")
    detail = JavaField("Ljava/lang/Throwable;")
    row = JavaField("I")
    getDetail = JavaMethod("()Ljava/lang/Throwable;")
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")
    printStackTrace = JavaMethod("()V")