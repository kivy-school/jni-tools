from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbki"]

class zzbki(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbki"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Object;I)V", False)]
    zzf = JavaStaticMethod("(Ljava/lang/String;Z)Lcom/google/android/gms/internal/ads/zzbkh;")