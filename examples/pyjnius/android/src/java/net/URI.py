from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URI"]

class URI(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URI"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/net/URI;)I", False, False)])
    isAbsolute = JavaMethod("()Z")
    resolve = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/net/URI;", False, False), ("(Ljava/net/URI;)Ljava/net/URI;", False, False)])
    create = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/URI;")
    getScheme = JavaMethod("()Ljava/lang/String;")
    isOpaque = JavaMethod("()Z")
    getRawAuthority = JavaMethod("()Ljava/lang/String;")
    getRawFragment = JavaMethod("()Ljava/lang/String;")
    getRawQuery = JavaMethod("()Ljava/lang/String;")
    getRawPath = JavaMethod("()Ljava/lang/String;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getAuthority = JavaMethod("()Ljava/lang/String;")
    getQuery = JavaMethod("()Ljava/lang/String;")
    getPath = JavaMethod("()Ljava/lang/String;")
    getUserInfo = JavaMethod("()Ljava/lang/String;")
    toURL = JavaMethod("()Ljava/net/URL;")
    normalize = JavaMethod("()Ljava/net/URI;")
    relativize = JavaMethod("(Ljava/net/URI;)Ljava/net/URI;")
    getRawSchemeSpecificPart = JavaMethod("()Ljava/lang/String;")
    parseServerAuthority = JavaMethod("()Ljava/net/URI;")
    getSchemeSpecificPart = JavaMethod("()Ljava/lang/String;")
    getRawUserInfo = JavaMethod("()Ljava/lang/String;")
    getFragment = JavaMethod("()Ljava/lang/String;")
    toASCIIString = JavaMethod("()Ljava/lang/String;")