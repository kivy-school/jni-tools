from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxySelector"]

class ProxySelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ProxySelector"
    __javaconstructor__ = [("()V", False)]
    select = JavaMethod("(Ljava/net/URI;)Ljava/util/List;")
    of = JavaStaticMethod("(Ljava/net/InetSocketAddress;)Ljava/net/ProxySelector;")
    getDefault = JavaStaticMethod("()Ljava/net/ProxySelector;")
    connectFailed = JavaMethod("(Ljava/net/URI;Ljava/net/SocketAddress;Ljava/io/IOException;)V")
    setDefault = JavaStaticMethod("(Ljava/net/ProxySelector;)V")