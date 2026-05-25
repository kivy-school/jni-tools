from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoadAdError"]

class LoadAdError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/LoadAdError"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;Lcom/google/android/gms/ads/AdError;Lcom/google/android/gms/ads/ResponseInfo;)V", False)]
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    toString = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("()Lorg/json/JSONObject;")