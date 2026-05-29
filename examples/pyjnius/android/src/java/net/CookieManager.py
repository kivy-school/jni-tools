from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieManager"]

class CookieManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CookieManager"
    __javaconstructor__ = [("()V", False), ("(Ljava/net/CookieStore;Ljava/net/CookiePolicy;)V", False)]
    setCookiePolicy = JavaMethod("(Ljava/net/CookiePolicy;)V")
    getCookieStore = JavaMethod("()Ljava/net/CookieStore;")
    get = JavaMethod("(Ljava/net/URI;Ljava/util/Map;)Ljava/util/Map;")
    put = JavaMethod("(Ljava/net/URI;Ljava/util/Map;)V")