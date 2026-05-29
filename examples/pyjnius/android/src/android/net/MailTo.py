from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MailTo"]

class MailTo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/MailTo"
    MAILTO_SCHEME = JavaStaticField("Ljava/lang/String;")
    getHeaders = JavaMethod("()Ljava/util/Map;")
    getSubject = JavaMethod("()Ljava/lang/String;")
    getTo = JavaMethod("()Ljava/lang/String;")
    isMailTo = JavaStaticMethod("(Ljava/lang/String;)Z")
    getCc = JavaMethod("()Ljava/lang/String;")
    getBody = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    parse = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/MailTo;")