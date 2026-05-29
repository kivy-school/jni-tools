from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLUtil"]

class URLUtil(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/URLUtil"
    __javaconstructor__ = [("()V", False)]
    composeSearchUrl = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    guessUrl = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    isAboutUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isAssetUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isContentUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    guessFileName = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    isCookielessProxyUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isDataUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isFileUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isHttpUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isHttpsUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isJavaScriptUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isNetworkUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isValidUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    stripAnchor = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    decode = JavaStaticMethod("([B)[B")