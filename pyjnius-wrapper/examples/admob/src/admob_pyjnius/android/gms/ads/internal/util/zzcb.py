from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcb"]

class zzcb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/zzcb"
    zza = JavaStaticMethod("(Landroid/content/Context;Ljava/util/concurrent/Callable;)Ljava/lang/Object;")