from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpCookie"]

class HttpCookie(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/HttpCookie"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    parse = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/List;")
    hasExpired = JavaMethod("()Z")
    setComment = JavaMethod("(Ljava/lang/String;)V")
    getComment = JavaMethod("()Ljava/lang/String;")
    setCommentURL = JavaMethod("(Ljava/lang/String;)V")
    getCommentURL = JavaMethod("()Ljava/lang/String;")
    setDiscard = JavaMethod("(Z)V")
    getDiscard = JavaMethod("()Z")
    setPortlist = JavaMethod("(Ljava/lang/String;)V")
    getPortlist = JavaMethod("()Ljava/lang/String;")
    setDomain = JavaMethod("(Ljava/lang/String;)V")
    getDomain = JavaMethod("()Ljava/lang/String;")
    setMaxAge = JavaMethod("(J)V")
    getMaxAge = JavaMethod("()J")
    setPath = JavaMethod("(Ljava/lang/String;)V")
    getPath = JavaMethod("()Ljava/lang/String;")
    setSecure = JavaMethod("(Z)V")
    getSecure = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    setValue = JavaMethod("(Ljava/lang/String;)V")
    getValue = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()I")
    setVersion = JavaMethod("(I)V")
    isHttpOnly = JavaMethod("()Z")
    setHttpOnly = JavaMethod("(Z)V")
    domainMatches = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")