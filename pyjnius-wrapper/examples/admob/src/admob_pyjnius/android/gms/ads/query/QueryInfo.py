from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QueryInfo"]

class QueryInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/query/QueryInfo"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zzex;)V", False)]
    getQuery = JavaMethod("()Ljava/lang/String;")
    getQueryBundle = JavaMethod("()Landroid/os/Bundle;")
    getRequestId = JavaMethod("()Ljava/lang/String;")
    generate = JavaMultipleMethod([("(Landroid/content/Context;Lcom/google/android/gms/ads/AdFormat;Lcom/google/android/gms/ads/AdRequest;Lcom/google/android/gms/ads/query/QueryInfoGenerationCallback;)V", True, False), ("(Landroid/content/Context;Lcom/google/android/gms/ads/AdFormat;Lcom/google/android/gms/ads/AdRequest;Ljava/lang/String;Lcom/google/android/gms/ads/query/QueryInfoGenerationCallback;)V", True, False)])