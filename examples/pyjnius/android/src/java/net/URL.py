from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URL"]

class URL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URL"
    __javaconstructor__ = [("(Ljava/net/URL;Ljava/lang/String;Ljava/net/URLStreamHandler;)V", False), ("(Ljava/net/URL;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/net/URLStreamHandler;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(Ljava/net/URI;Ljava/net/URLStreamHandler;)Ljava/net/URL;")
    openStream = JavaMethod("()Ljava/io/InputStream;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getDefaultPort = JavaMethod("()I")
    sameFile = JavaMethod("(Ljava/net/URL;)Z")
    toExternalForm = JavaMethod("()Ljava/lang/String;")
    openConnection = JavaMultipleMethod([("(Ljava/net/Proxy;)Ljava/net/URLConnection;", False, False), ("()Ljava/net/URLConnection;", False, False)])
    getContent = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("([Ljava/lang/Class;)Ljava/lang/Object;", False, False)])
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getAuthority = JavaMethod("()Ljava/lang/String;")
    getFile = JavaMethod("()Ljava/lang/String;")
    getRef = JavaMethod("()Ljava/lang/String;")
    getQuery = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("()Ljava/lang/String;")
    getUserInfo = JavaMethod("()Ljava/lang/String;")
    toURI = JavaMethod("()Ljava/net/URI;")
    setURLStreamHandlerFactory = JavaStaticMethod("(Ljava/net/URLStreamHandlerFactory;)V")