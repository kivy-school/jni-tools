from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieHandler"]

class CookieHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CookieHandler"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljava/net/CookieHandler;")
    setDefault = JavaStaticMethod("(Ljava/net/CookieHandler;)V")
    get = JavaMethod("(Ljava/net/URI;Ljava/util/Map;)Ljava/util/Map;")
    put = JavaMethod("(Ljava/net/URI;Ljava/util/Map;)V")