from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieStore"]

class CookieStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CookieStore"
    remove = JavaMethod("(Ljava/net/URI;Ljava/net/HttpCookie;)Z")
    add = JavaMethod("(Ljava/net/URI;Ljava/net/HttpCookie;)V")
    get = JavaMethod("(Ljava/net/URI;)Ljava/util/List;")
    getCookies = JavaMethod("()Ljava/util/List;")
    getURIs = JavaMethod("()Ljava/util/List;")
    removeAll = JavaMethod("()Z")