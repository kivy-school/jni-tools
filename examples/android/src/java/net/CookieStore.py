from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieStore"]

class CookieStore(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CookieStore"
    add = JavaMethod("(Ljava/net/URI;Ljava/net/HttpCookie;)V")
    get = JavaMethod("(Ljava/net/URI;)Ljava/util/List;")
    getCookies = JavaMethod("()Ljava/util/List;")
    getURIs = JavaMethod("()Ljava/util/List;")
    remove = JavaMethod("(Ljava/net/URI;Ljava/net/HttpCookie;)Z")
    removeAll = JavaMethod("()Z")