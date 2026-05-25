from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLUtil"]

class URLUtil(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/URLUtil"
    __javaconstructor__ = [("()V", False)]
    guessUrl = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    composeSearchUrl = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    decode = JavaStaticMethod("([B)[B")
    isAssetUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isCookielessProxyUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isFileUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isAboutUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isDataUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isJavaScriptUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isHttpUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isHttpsUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isNetworkUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isContentUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    isValidUrl = JavaStaticMethod("(Ljava/lang/String;)Z")
    stripAnchor = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    guessFileName = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")