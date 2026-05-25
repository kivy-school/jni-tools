from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdg"]

class zzcdg(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdg"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/rewarded/RewardItem;)V", False), ("(Ljava/lang/String;I)V", False)]
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()I")