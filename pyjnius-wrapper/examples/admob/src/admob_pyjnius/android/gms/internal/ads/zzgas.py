from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgas"]

class zzgas(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgas"
    zzf = JavaMethod("(Ljava/net/URL;I)Ljava/net/URLConnection;")
    zzg = JavaMethod("(Landroid/net/Network;Ljava/net/URL;II)Ljava/net/HttpURLConnection;")
    zzh = JavaMethod("(Lcom/google/android/gms/internal/ads/zzgai;II)Ljava/net/HttpURLConnection;")
    zzi = JavaStaticMethod("(Ljava/net/HttpURLConnection;)V")
    zzj = JavaMethod("()Ljava/net/HttpURLConnection;")
    close = JavaMethod("()V")