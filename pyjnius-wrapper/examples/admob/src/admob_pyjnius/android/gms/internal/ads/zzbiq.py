from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbiq"]

class zzbiq(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbiq"
    __javaconstructor__ = [("()V", False)]
    zza = JavaStaticMethod("(Landroid/content/Context;)Landroid/content/SharedPreferences;")
    zzb = JavaStaticMethod("(Landroid/content/Context;)Landroid/content/SharedPreferences;")