from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MailTo"]

class MailTo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/MailTo"
    MAILTO_SCHEME = JavaStaticField("Ljava/lang/String;")
    isMailTo = JavaStaticMethod("(Ljava/lang/String;)Z")
    parse = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/MailTo;")
    getTo = JavaMethod("()Ljava/lang/String;")
    getCc = JavaMethod("()Ljava/lang/String;")
    getSubject = JavaMethod("()Ljava/lang/String;")
    getBody = JavaMethod("()Ljava/lang/String;")
    getHeaders = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")