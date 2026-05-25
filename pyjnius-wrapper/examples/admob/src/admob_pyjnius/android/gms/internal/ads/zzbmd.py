from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmd"]

class zzbmd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmd"
    __javaconstructor__ = [("()V", False)]
    zzj = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/internal/ads/zzbme;")
    zzdd = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")