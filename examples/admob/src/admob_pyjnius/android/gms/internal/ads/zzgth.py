from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgth"]

class zzgth(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgth"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Ljava/lang/CharSequence;)Lcom/google/android/gms/internal/ads/zzgtg;")