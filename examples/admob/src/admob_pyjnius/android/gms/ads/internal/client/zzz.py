from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzz"]

class zzz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzz"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    zza = JavaMethod("(Z)[Lcom/google/android/gms/ads/AdSize;")
    zzb = JavaMethod("()Ljava/lang/String;")