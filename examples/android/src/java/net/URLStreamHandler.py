from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLStreamHandler"]

class URLStreamHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLStreamHandler"
    __javaconstructor__ = [("()V", False)]
    openConnection = JavaMultipleMethod([("(Ljava/net/URL;)Ljava/net/URLConnection;", False, False), ("(Ljava/net/URL;Ljava/net/Proxy;)Ljava/net/URLConnection;", False, False)])
    parseURL = JavaMethod("(Ljava/net/URL;Ljava/lang/String;II)V")
    getDefaultPort = JavaMethod("()I")
    equals = JavaMethod("(Ljava/net/URL;Ljava/net/URL;)Z")
    hashCode = JavaMethod("(Ljava/net/URL;)I")
    sameFile = JavaMethod("(Ljava/net/URL;Ljava/net/URL;)Z")
    getHostAddress = JavaMethod("(Ljava/net/URL;)Ljava/net/InetAddress;")
    hostsEqual = JavaMethod("(Ljava/net/URL;Ljava/net/URL;)Z")
    toExternalForm = JavaMethod("(Ljava/net/URL;)Ljava/lang/String;")
    setURL = JavaMultipleMethod([("(Ljava/net/URL;Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/net/URL;Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;)V", False, False)])