from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URI"]

class URI(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URI"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    create = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/URI;")
    parseServerAuthority = JavaMethod("()Ljava/net/URI;")
    normalize = JavaMethod("()Ljava/net/URI;")
    resolve = JavaMultipleMethod([("(Ljava/net/URI;)Ljava/net/URI;", False, False), ("(Ljava/lang/String;)Ljava/net/URI;", False, False)])
    relativize = JavaMethod("(Ljava/net/URI;)Ljava/net/URI;")
    toURL = JavaMethod("()Ljava/net/URL;")
    getScheme = JavaMethod("()Ljava/lang/String;")
    isAbsolute = JavaMethod("()Z")
    isOpaque = JavaMethod("()Z")
    getRawSchemeSpecificPart = JavaMethod("()Ljava/lang/String;")
    getSchemeSpecificPart = JavaMethod("()Ljava/lang/String;")
    getRawAuthority = JavaMethod("()Ljava/lang/String;")
    getAuthority = JavaMethod("()Ljava/lang/String;")
    getRawUserInfo = JavaMethod("()Ljava/lang/String;")
    getUserInfo = JavaMethod("()Ljava/lang/String;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getRawPath = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("()Ljava/lang/String;")
    getRawQuery = JavaMethod("()Ljava/lang/String;")
    getQuery = JavaMethod("()Ljava/lang/String;")
    getRawFragment = JavaMethod("()Ljava/lang/String;")
    getFragment = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    compareTo = JavaMethod("(Ljava/net/URI;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    toASCIIString = JavaMethod("()Ljava/lang/String;")