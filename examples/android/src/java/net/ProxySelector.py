from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxySelector"]

class ProxySelector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ProxySelector"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljava/net/ProxySelector;")
    setDefault = JavaStaticMethod("(Ljava/net/ProxySelector;)V")
    select = JavaMethod("(Ljava/net/URI;)Ljava/util/List;")
    connectFailed = JavaMethod("(Ljava/net/URI;Ljava/net/SocketAddress;Ljava/io/IOException;)V")