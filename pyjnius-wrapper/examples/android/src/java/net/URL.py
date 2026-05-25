from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URL"]

class URL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URL"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/net/URLStreamHandler;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/net/URL;Ljava/lang/String;)V", False), ("(Ljava/net/URL;Ljava/lang/String;Ljava/net/URLStreamHandler;)V", False)]
    getQuery = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("()Ljava/lang/String;")
    getUserInfo = JavaMethod("()Ljava/lang/String;")
    getAuthority = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getDefaultPort = JavaMethod("()I")
    getProtocol = JavaMethod("()Ljava/lang/String;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getFile = JavaMethod("()Ljava/lang/String;")
    getRef = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    sameFile = JavaMethod("(Ljava/net/URL;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    toExternalForm = JavaMethod("()Ljava/lang/String;")
    toURI = JavaMethod("()Ljava/net/URI;")
    openConnection = JavaMultipleMethod([("()Ljava/net/URLConnection;", False, False), ("(Ljava/net/Proxy;)Ljava/net/URLConnection;", False, False)])
    openStream = JavaMethod("()Ljava/io/InputStream;")
    getContent = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("([Ljava/lang/Class;)Ljava/lang/Object;", False, False)])
    setURLStreamHandlerFactory = JavaStaticMethod("(Ljava/net/URLStreamHandlerFactory;)V")