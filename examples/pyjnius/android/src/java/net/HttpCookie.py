from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpCookie"]

class HttpCookie(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/HttpCookie"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    setVersion = JavaMethod("(I)V")
    setDomain = JavaMethod("(Ljava/lang/String;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    getValue = JavaMethod("()Ljava/lang/String;")
    setValue = JavaMethod("(Ljava/lang/String;)V")
    parse = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/List;")
    getPath = JavaMethod("()Ljava/lang/String;")
    getDomain = JavaMethod("()Ljava/lang/String;")
    setSecure = JavaMethod("(Z)V")
    setPath = JavaMethod("(Ljava/lang/String;)V")
    getVersion = JavaMethod("()I")
    getComment = JavaMethod("()Ljava/lang/String;")
    hasExpired = JavaMethod("()Z")
    getMaxAge = JavaMethod("()J")
    getPortlist = JavaMethod("()Ljava/lang/String;")
    setCommentURL = JavaMethod("(Ljava/lang/String;)V")
    getCommentURL = JavaMethod("()Ljava/lang/String;")
    setDiscard = JavaMethod("(Z)V")
    getDiscard = JavaMethod("()Z")
    setPortlist = JavaMethod("(Ljava/lang/String;)V")
    setMaxAge = JavaMethod("(J)V")
    getSecure = JavaMethod("()Z")
    isHttpOnly = JavaMethod("()Z")
    setHttpOnly = JavaMethod("(Z)V")
    domainMatches = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    setComment = JavaMethod("(Ljava/lang/String;)V")