from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookiePolicy"]

class CookiePolicy(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CookiePolicy"
    ACCEPT_ALL = JavaStaticField("Ljava/net/CookiePolicy;")
    ACCEPT_NONE = JavaStaticField("Ljava/net/CookiePolicy;")
    ACCEPT_ORIGINAL_SERVER = JavaStaticField("Ljava/net/CookiePolicy;")
    shouldAccept = JavaMethod("(Ljava/net/URI;Ljava/net/HttpCookie;)Z")