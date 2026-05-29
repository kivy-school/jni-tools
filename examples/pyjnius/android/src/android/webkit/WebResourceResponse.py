from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebResourceResponse"]

class WebResourceResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebResourceResponse"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/util/Map;Ljava/io/InputStream;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/io/InputStream;)V", False)]
    getReasonPhrase = JavaMethod("()Ljava/lang/String;")
    getResponseHeaders = JavaMethod("()Ljava/util/Map;")
    getStatusCode = JavaMethod("()I")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    setMimeType = JavaMethod("(Ljava/lang/String;)V")
    setResponseHeaders = JavaMethod("(Ljava/util/Map;)V")
    setStatusCodeAndReasonPhrase = JavaMethod("(ILjava/lang/String;)V")
    setData = JavaMethod("(Ljava/io/InputStream;)V")
    getData = JavaMethod("()Ljava/io/InputStream;")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    getMimeType = JavaMethod("()Ljava/lang/String;")