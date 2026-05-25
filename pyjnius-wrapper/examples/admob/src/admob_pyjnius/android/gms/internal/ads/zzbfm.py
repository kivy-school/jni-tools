from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbfm"]

class zzbfm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbfm"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/admanager/AppEventListener;)V", False)]
    zzb = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    zzc = JavaMethod("()Lcom/google/android/gms/ads/admanager/AppEventListener;")