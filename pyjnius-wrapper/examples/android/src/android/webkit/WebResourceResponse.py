from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebResourceResponse"]

class WebResourceResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebResourceResponse"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/io/InputStream;)V", False), ("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/util/Map;Ljava/io/InputStream;)V", False)]
    setMimeType = JavaMethod("(Ljava/lang/String;)V")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setStatusCodeAndReasonPhrase = JavaMethod("(ILjava/lang/String;)V")
    getStatusCode = JavaMethod("()I")
    getReasonPhrase = JavaMethod("()Ljava/lang/String;")
    setResponseHeaders = JavaMethod("(Ljava/util/Map;)V")
    getResponseHeaders = JavaMethod("()Ljava/util/Map;")
    setData = JavaMethod("(Ljava/io/InputStream;)V")
    getData = JavaMethod("()Ljava/io/InputStream;")